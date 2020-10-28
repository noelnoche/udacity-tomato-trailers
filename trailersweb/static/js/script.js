$(document).ready(function () {

  function removeVideoContent() {
    // Remove the src so the player itself gets removed, as this is the 
    // only reliable way to ensure the video stops playing in IE
    $('#trailer-video').attr('src', '');
    $('#trailer-video-container').empty();
    $('.movie-info').remove();
  }

  $('.close-btn').on('click', function (e) {
    removeVideoContent();
  });


  function addVideoContent(curMovieTile) {
    removeVideoContent();
    var trailerYouTubeId = curMovieTile.attr('data-trailer-youtube-id')
    var storyline = curMovieTile.attr('data-storyline')
    var link = curMovieTile.attr('data-link')
    var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';

    $('#trailer-video-container').empty().append($('<iframe></iframe>', {
      'id': 'trailer-video',
      'type': 'text-html',
      'src': sourceUrl,
      'frameborder': 0
    }));

    var element = '<div class="movie-info"><p>STORY: ' + storyline +
      '</p><hr><a href="' + link + '">IMDb Link: ' + link + '</a></div>';
    $('.modal-content').append(element)
  }

  var $movieTile = $('.movie-tile');

  $movieTile.on('click', function () {
    addVideoContent($(this));
  });


  // Animate in the movies when the page loads
  $(document).ready(function () {
    $movieTile.hide().first().show('fast', function showNext() {
      $(this).next('div').show('fast', showNext);
    });
  });
});
