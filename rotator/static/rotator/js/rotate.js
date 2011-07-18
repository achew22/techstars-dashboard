function setPage(urls, frame) {
    // Siwtch out the preloaded page
    var base_page = "#page";
    $(base_page+frame)
        .show();
    $(base_page+(frame^1))
        .hide()

    var current = urls.shift();
    var timeout = current[1];

    if (urls.length) {
        // Load the next url up
        var next_url = urls[0][0];

        // Preload the next frame
        $(base_page+(frame^1))
            .attr('src', next_url);
    } else {
        // If we are at the end of the loop, 
        // reload the loop list after the timeout
        setTimeout(function() {
            $.getJSON('/rotator/leafs/', start);
        }, timeout);
        return; // Reload everything and start again
    }


    // Recurse recurse
    setTimeout(function() {
        setPage(urls, frame^1);
    }, timeout);
}

function start(data) {
    // Set #page0 so that when we enter the loop again it gets preloaded
    $('#page0')
        .hide();
    $('#page1')
        .attr('src', data[0][0])
        .show();
    setPage(data,0);
}

$(document).ready(function() {
    $.getJSON('/rotator/leafs/', start);
});
