$(document).ready(function() {
        urls = [
                //['/countdown/', 30 * 1000],
                ['http://visibletweets.com/#query=techstars&animation=2',   30 * 1000],
                ['/calendar/?id=0', 8  * 1000],
                ['/calendar/?id=1', 8  * 1000],
             	['/calendar/?id=2', 8  * 1000],
                ['/calendar/?id=3', 8  * 1000],
        ];
        function setPage(index,frame) {
                var next = index+1;
                if (next >= urls.length) {
                        next = 0;
                }
                timeout = urls[index][1];

                // Set the page
                var page = "#page";
                $(page+frame)
                  .show();
                $(page+(frame^1))
                  .hide()
                  .attr('src', urls[next][0]);

                setTimeout(function() {
                        setPage(next, frame^1);
                }, timeout)
        }
        $('#page0').attr('src', urls[0][0]);
	setPage(0,0);
});
