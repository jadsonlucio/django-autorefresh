console.warn = () => { };

var successive_errors = 0

function checkRefresh() {
    try {
        var req = new XMLHttpRequest();
        req.open('GET', '/fresh/', false);
        req.send();
        var fresh = JSON.parse(req.responseText).fresh;
        if (fresh) location.reload();
        successive_errors = 0;
        doPoll();
    } catch (e) {
        successive_errors++;
        if (successive_errors < 10) {
            doPoll();
        }


    }
}

function doPoll() {
    setTimeout(function () {
        checkRefresh();
    }, 1000);
}

doPoll();

