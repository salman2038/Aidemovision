import streamlit as st
import streamlit.components.v1 as components
# bootstrap 4 collapse example
components.html(
    """
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    <style>
    /*Google Fonts*/
.tajawal-extralight {
  font-family: "Tajawal", sans-serif;
  font-weight: 200;
  font-style: normal;
}

.tajawal-light {
  font-family: "Tajawal", sans-serif;
  font-weight: 300;
  font-style: normal;
}

.tajawal-regular {
  font-family: "Tajawal", sans-serif;
  font-weight: 400;
  font-style: normal;
}

.tajawal-medium {
  font-family: "Tajawal", sans-serif;
  font-weight: 500;
  font-style: normal;
}

.tajawal-bold {
  font-family: "Tajawal", sans-serif;
  font-weight: 700;
  font-style: normal;
}

.tajawal-extrabold {
  font-family: "Tajawal", sans-serif;
  font-weight: 800;
  font-style: normal;
}

.tajawal-black {
  font-family: "Tajawal", sans-serif;
  font-weight: 900;
  font-style: normal;
}

/*Global Css*/
body{
  font-family: "Tajawal", sans-serif !important;
  font-weight: 400 !important;
  font-style: normal;
}
/* width */
::-webkit-scrollbar {
  width: 6px;
}

/* Track */
::-webkit-scrollbar-track {
  background: #f1f1f1; 
}
     
/* Handle */
::-webkit-scrollbar-thumb {
  background: #9c7d3f ; 
}

/* Handle on hover */
::-webkit-scrollbar-thumb:hover {
   background: #1c3a5f ; 
}

/* EndGlobal Css */

.logo {
    padding: 50px 0px;
    text-align: center;
    width: 300px;
}

.logo img {object-fit: contain;}

.wrapper {
    width: 100%;
    text-align: center;
    display: flex;
    justify-content: center;
    align-items: center;
}

section.Icon-Area {}

.Icon-Box {
    width: 100%;
    text-align: center;
}

.Icon-Box ul {}

.Icon-Box ul li {
    width: 76px;
    height: 76px;
    margin-left: 20px;
}

.Icon-Box ul li img {
    height: 100%;
    width: 100%;
    object-fit: contain;
}

.Button-Box {
    text-align: end;
}

.Button-Box #playButton {
    background: #7303c0;
    padding: 7px 40px;
    border: none;
}

.Button-Box #stopButton {
    background: #000;
    padding: 7px 40px;
    border: none;
}

.video-box {
    border-radius: 30px;
    width: 100%;
    height: 100%;
    margin-top: 0px;
}

.video-box video {
    border-radius: 20px;
    width: 100% !important;
    height: 100% !important;
    margin-top: 0px;
}

section.Footer-Logo {}

.Footer-Logo {
    height: 60px;
    width: 100%;
    margin-top: 30px;
}

.Footer-Logo a img {
    width: 100%;
    height: 100%;
    object-fit: contain;
}
section.Footer-Area {padding: 50px 0 20px;}
.Btn-Box {
    text-align: end;
}

.form-drop-field {}

.form-drop-field label {
    width: 26%;
    text-align: right;
    margin-right: 10px;
}

.form-drop-field select {
    padding: 7px 30px 7px 7px;
    width: 67%;
}

.form-drop-field select option {
    font-size: 16px;
    font-weight: 300;
}

.Btn-Box button {
    color: #5B0092;
    background: transparent;
    border-color: #5B0092;
    padding: 5px 20px;
}
section.Video-Area {
    margin-top: -70px;
}
    </style>
    <body>

<div class="wrapper">
		 <div class="logo"><a href="#"><img src="data:image/png;base64,{images/logo.png}" class="img-fluid"></a></div>
</div>
<section class="Form-Area">
	<div class="container">
        <form>
        	<div class="row">
        		<div class="col-12 col-lg-4 col-md-6 col-sm-12">
        			 <div class="mb-3 form-drop-field">
                <label for="sourceType" class="form-label">Source Type</label>
                <select class="form-select" id="sourceType" required>
                    <option value="" disabled selected>Select Source Type</option>
                    <option value="video">Video</option>
                    <option value="rtsp">RTSP</option>
                    <option value="cam">Cam</option>
                </select>
            </div>
        		</div>
        		<div class="col-12 col-lg-4 col-md-6 col-sm-12">
        			 <div class="mb-3 form-drop-field">
                <label for="useCase" class="form-label">Use Case</label>
                <select class="form-select" id="useCase" required>
                    <option value="" disabled selected>Select Use Case</option>
                    <option value="ppe-compliance">PPE Compliance</option>
                    <option value="incident">Incident</option>
                    <option value="smoke">Smoke</option>
                    <option value="fire">Fire</option>
                </select>
            </div>
        		</div>
        		<div class="col-12 col-lg-4 col-md-6 col-sm-12">
        			  <div class="mb-3 form-drop-field">
                <label for="videos" class="form-label">Videos</label>
                <select class="form-select" id="videos" required>
              <option value="" disabled selected>Select Use Case</option>
                    <option value="ppe-compliance">PPE Compliance</option>
                    <option value="incident">Incident</option>
                    <option value="smoke">Smoke</option>
                    <option value="fire">Fire</option>
                </select>
            </div>
        		</div>
        		<div class="col-12 col-a=sm-12">  
        			<div class="Btn-Box">
        			<button type="submit" class="btn btn-primary">Submit</button>
        			</div>
        		</div>
           </div>

           

          

          
        </form>
    </div>

</section>

<section class="Icon-Area">
	<div class="container">
		<div class="row">
			<div class="Icon-Box">
				<ul class="list-unstyled list-inline">
					<li class="list-inline-item">
						<img src="Images/icon-1.svg" class="img-fluid">
					</li>
					<li class="list-inline-item">
						<img src="Images/icon-2.svg" class="img-fluid">
					</li>
					<li class="list-inline-item">
						<img src="Images/icon-3.svg" class="img-fluid">
					</li>
				</ul>
			</div>
		</div>
	</div>
</section>
<section class="Video-Area">
	
	<div class="container">
        <div class="row">
            <div class="col-12 col-lg-12 col-md-12">
            	<div class="Button-Box">
            		  <button id="playButton" class="btn btn-primary">Play</button>
                    <button id="stopButton" class="btn btn-danger">Stop</button>
            	</div>
                <div class="embed-responsive embed-responsive-16by9 video-box">
                    <video id="myVideo" class="embed-responsive-item" controls>
                        <source src="https://www.w3schools.com/html/mov_bbb.mp4" type="video/mp4">
                        Your browser does not support the video tag.
                    </video>
                </div>
               
            </div>
        </div>
    </div>
</section>
<section class="Footer-Area">
	<div class="container">
		<div class="row">
			<div class="Footer-Logo">
				<a href="#">
					<img src="https://www.veraqor.io/wp-content/uploads/2022/09/web-logo-old-01-1.svg" class="img-fluid"> 
				</a>
			</div>
		</div>
	</div>
</section>
</body>
    <!-- Custom JS -->
    <script>
        document.getElementById('playButton').addEventListener('click', function() {
            var video = document.getElementById('myVideo');
            if (video.paused || video.ended) {
                video.play();
            }
        });

        document.getElementById('stopButton').addEventListener('click', function() {
            var video = document.getElementById('myVideo');
            video.pause();
            video.currentTime = 0; // Reset video to start
        });
    </script>
    """,
    height=800,
)
