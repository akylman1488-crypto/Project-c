const fs = require('fs');
const https = require('https');
const path = require('path');

const outputFile = path.join(__dirname, 'network_data.json');
const sources = ['https://api.coindesk.com/v1/bpi/currentprice.json'];

async function scan() {
    try {
        const data = await new Promise((resolve, reject) => {
            https.get(sources[0], (res) => {
                let data = '';
                res.on('data', chunk => data += chunk);
                res.on('end', () => resolve(JSON.parse(data)));
            }).on('error', reject);
        });

        fs.writeFileSync(outputFile, JSON.stringify({
            timestamp: Date.now(),
            btc_price: data.bpi.USD.rate
        }));
    } catch (e) {
        console.error(e.message);
    }
}

setInterval(scan, 10000);
scan();
