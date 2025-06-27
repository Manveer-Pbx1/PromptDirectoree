
async function sendRequest(method) {
    const url = document.getElementById('url').value;
    const body = document.getElementById('body').value;
    const responseBox = document.getElementById('response');

    try {
        const options = {
            method,
            headers: {
                'Content-Type': 'application/json'
            }
        };

        if (method === 'POST' || method === 'PUT') {
            options.body = body;
        }

        const res = await fetch(url, options);
        const text = await res.text();

        responseBox.textContent = `Status: ${res.status} ${res.statusText}\n\n${text}`;
    } catch (err) {
        responseBox.textContent = `Error: ${err.message}`;
    }
}
