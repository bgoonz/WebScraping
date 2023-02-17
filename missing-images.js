const puppeteer = require('puppeteer');
const cheerio = require('cheerio');
// const browser = await puppeteer.launch({
//     executablePath: '/usr/bin/chromium-browser'
//   })
const url = 'https://bgoonz-blog.netlify.app/blog/';
const missingImages = [];

async function scrapePage(page) {
  const content = await page.content();
  const $ = cheerio.load(content);

  $('img').each(function() {
    const src = $(this).attr('src');
    if (!src) {
      missingImages.push({
        url: page.url(),
        selector: this.attribs.class || this.attribs.id
      });
    }
  });
}

async function scrapeSite() {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto(url, { waitUntil: 'networkidle2' });

  await scrapePage(page);

  const links = await page.$$eval('a', as => as.map(a => a.href));
  for (let link of links) {
    const newPage = await browser.newPage();
    await newPage.goto(link, { waitUntil: 'networkidle2' });
    await scrapePage(newPage);
    await newPage.close();
  }

  await browser.close();

  console.log('Missing images:');
  console.log(missingImages);
}

scrapeSite();
