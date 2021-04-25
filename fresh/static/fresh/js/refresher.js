console.warn = () => { };

function checkRefresh() {

    var response = false;
    while (!response) {
        try {
            var req = new XMLHttpRequest();
            req.open('GET', '/fresh/', false);
            req.send();
            response = true;
            var fresh = JSON.parse(req.responseText).fresh;
            if (fresh) location.reload();
        } catch (e) {
            location.reload();
        }

    }



    doPoll();
}

function doPoll() {
    setTimeout(function () {
        checkRefresh();
    }, 1000);
}

doPoll();

