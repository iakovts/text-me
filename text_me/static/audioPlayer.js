var audio = document.getElementById('audio');
        var playButton = document.getElementById('play');
        var pauseButton = document.getElementById('pause');
        var volumeSlider = document.getElementById('volume');
        var volumeUpButton = document.querySelector('.fa-volume-up');
        var previousVolume = audio.volume;
        var streamUrl = audio.src;

        playButton.addEventListener('click', function(){
            audio.play();
        });
    
        pauseButton.addEventListener('click', function(){
            audio.pause();
            audio.src = streamUrl;

        });

        volumeSlider.addEventListener('input', function(){
            audio.volume = volumeSlider.value;
        });

        volumeSlider.addEventListener('input', function(){
            audio.volume = this.value;
            if(audio.volume == 0){
                volumeUpButton.classList.remove('fa-volume-up');
                volumeUpButton.classList.add('fa-volume-off');
            } else {
                volumeUpButton.classList.remove('fa-volume-off');
                volumeUpButton.classList.add('fa-volume-up');
            }
        });

        volumeUpButton.addEventListener('click', function() {
            if (audio.volume > 0) {
                previousVolume = audio.volume;
                audio.volume = 0;
                volumeUpButton.classList.remove('fa-volume-up');
                volumeUpButton.classList.add('fa-volume-off');
            } else {
                audio.volume = previousVolume;
                volumeUpButton.classList.remove('fa-volume-off');
                volumeUpButton.classList.add('fa-volume-up');
            }
        });   