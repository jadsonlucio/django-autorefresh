var successive_errors = 0;
var max_sucessive_errors = 600; // 10 minutes

function makeRequest(url) {
    return new Promise(function (resolve, reject) {
        const xhr = new XMLHttpRequest();
        xhr.open('GET', url, true);
        xhr.responseType = 'json';
        xhr.onload = function () {
            const status = xhr.status;
            if (status == 200) {
                resolve(xhr.response);
            } else {
                reject(status);
            }
        };
        xhr.onerror = function (e) {
            reject(e);
        }
        xhr.send();
    });
}

async function checkRefresh() {
    try {
        const response = await makeRequest('/fresh/');
        if (response.fresh) {
            location.reload();
        }
        successive_errors = 0;
        doPoll();
    } catch (e) {
        successive_errors++;
        if (successive_errors < max_sucessive_errors) {
            doPoll();
        }
    }
}

function doPoll() {
    setTimeout(function () {
        checkRefresh();
    }, 1000);
}

document.addEventListener("DOMContentLoaded", function () {
    doPoll();
});
