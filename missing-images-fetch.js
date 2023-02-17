const fetch = require("node-fetch");
// Replace the URL with the website you want to scrape
const websiteUrl = 'https://bgoonz-blog.netlify.app/blog/';

fetch(websiteUrl)
  .then(response => response.text())
  .then(html => {
    const parser = new DOMParser();
    const doc = parser.parseFromString(html, 'text/html');
    const images = doc.querySelectorAll('img');
    const missingImages = Array.from(images).filter(image => image.hasAttribute('src') && image.getAttribute('onerror'));
    const missingImageSrcs = missingImages.map(image => image.getAttribute('src'));
    console.log('Missing images:', missingImageSrcs);
  })
  .catch(error => console.error(error));
