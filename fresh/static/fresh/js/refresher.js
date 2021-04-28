console.warn = () => { };

var successive_errors = 0
var max_sucessive_errors = 7200 // aproximily 2 hours

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

doPoll();

