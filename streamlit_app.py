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
.Icon-Box ul li svg {
    width: 100%;
    height: 100%;
    object-fit: contain;
}
/*Resposive Css*/
@media only screen and (min-width: 1025px) and (max-width: 1200px)  {
.form-drop-field label {
    width: 35%;
    text-align: left;
    margin-right: 10px;
}
.form-drop-field select {
    width: 100%;
}
}
 
@media only screen and (min-width: 992px) and (max-width: 1024px)  {
.form-drop-field label {
    width: 35%;
    text-align: left;
    margin-right: 10px;
}
.form-drop-field select {
    width: 100%;
}
}
@media only screen and (min-width: 768px) and (max-width: 991px)  {
    .form-drop-field select {
    width: 80%;
}
   .form-drop-field label {
    width: 15%;
    text-align: left;
    margin-right: 10px;
}
section.Video-Area {
    margin-top: 0px;
}
 
    }
@media only screen and (min-width: 200px) and (max-width: 767px)  {
.form-drop-field select {
    width: 100%;
}
.form-drop-field label {
    width: 35%;
    text-align: left;
    margin-right: 10px;
}
section.Main-body {
    margin: 30px 10px;
}
.logo {
    padding: 34px 0px;
    width: 200px;
}
.Icon-Box {
    text-align: left;
}
.Icon-Box ul li {
    width: 60px;
    height: 60px;
    margin-left: 20px;
}
.Btn-Box {
    text-align: justify;
}
.Button-Box {
    text-align: center;
}
section.Video-Area {
    margin-top: 0px;
}
section.Icon-Area {
    padding: 35px 0;
}
    }
    </style>
    <body>

<div class="wrapper">
		 <div class="logo"><a href="#"><img src="https://www.veraqor.io/wp-content/uploads/2024/09/logo.png" class="img-fluid"></a></div>
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
						<svg width="76" height="76" viewBox="0 0 76 76" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M41.8836 69.6947H28.8617C28.3045 69.6947 27.8501 69.2404 27.8501 68.6831V50.9471C27.8501 50.9471 27.7756 50.9471 27.6264 50.9471C24.5234 50.9471 21.9693 48.521 21.9843 45.5566L22.0526 31.9496C22.078 26.8782 27.8313 26.2025 31.9369 25.7661V20.2015L38.38 19.1595V25.7782C40.6932 26.029 42.3581 26.873 44.7877 26.3832C49.4073 25.4517 52.669 21.0032 55.6477 17.9858C56.4563 17.167 57.5022 16.8471 58.9683 17.7011C61.924 19.4234 56.932 24.9511 55.2453 26.5214C51.7401 29.7875 46.2663 33.0365 42.958 33.0345L42.8953 68.6848C42.8941 69.2416 42.4402 69.6947 41.8836 69.6947Z" fill="#60B7FF"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M27.8501 47.7233V68.6831C27.8501 69.2402 28.3045 69.6947 28.8617 69.6947H41.8836C42.4401 69.6947 42.8941 69.2416 42.8952 68.6849L42.932 47.7233H27.8501Z" fill="#837683"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M27.8501 47.7233V68.6831C27.8501 69.2402 28.3045 69.6947 28.8617 69.6947H29.199V47.7233H27.8501Z" fill="#685E68"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M30.4974 25.9287C30.9911 25.8675 31.4744 25.8153 31.9368 25.7661V20.2015L38.3799 19.1595V25.7782C38.8669 25.831 39.3253 25.9101 39.768 25.9976C38.6338 27.5713 36.9912 28.5615 35.1583 28.5615C33.3123 28.5615 31.6326 27.529 30.4974 25.9287Z" fill="#F1CBBC"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M31.9368 22.7116V20.2015L38.3798 19.1595V22.7116C37.4246 23.4046 36.3267 23.7996 35.1583 23.7996C33.9901 23.7996 32.8921 23.4046 31.9368 22.7116Z" fill="#F1CBBC"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M35.1585 8.07922C38.8452 8.07922 41.834 10.1804 41.834 15.0259C41.834 19.8715 38.8452 23.7996 35.1585 23.7996C31.4714 23.7996 28.4828 19.8715 28.4828 15.0259C28.4828 10.1804 31.4716 8.07922 35.1585 8.07922Z" fill="#F6DCCD"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M41.4984 2.37595C41.6174 4.26972 39.7541 4.89998 38.677 4.89998H32.8189C31.5669 4.89998 31.4198 6.06655 31.4198 6.56412H30.9568C28.4046 6.56412 26.6488 8.33869 27.2705 10.8676L28.5192 15.947L30.4591 11.0382C31.536 11.5804 32.968 12.0094 34.5708 12.2184C36.8438 12.5147 38.9162 12.2978 40.1918 11.7256L41.7976 15.947C45.2185 11.7156 42.9912 3.43728 41.4984 2.37595Z" fill="#837683"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M42.8932 67.019C44.3711 67.019 45.5691 68.217 45.5691 69.6949C45.5691 71.1727 44.3711 72.3708 42.8932 72.3708C41.4154 72.3708 40.2174 71.1727 40.2174 69.6949C40.2175 68.2169 41.4154 67.019 42.8932 67.019ZM42.6682 23.833C44.1461 23.833 45.3441 25.0311 45.3441 26.5089C45.3441 27.9868 44.1461 29.1848 42.6682 29.1848C41.1904 29.1848 39.9923 27.9868 39.9923 26.5089C39.9923 25.0311 41.1904 23.833 42.6682 23.833ZM55.245 23.8458C56.7229 23.8458 57.9209 25.0438 57.9209 26.5217C57.9209 27.9995 56.7229 29.1976 55.245 29.1976C53.7672 29.1976 52.5691 27.9995 52.5691 26.5217C52.5693 25.0438 53.7672 23.8458 55.245 23.8458ZM28.2301 31.4379C29.708 31.4379 30.906 32.636 30.906 34.1138C30.906 35.5917 29.708 36.7897 28.2301 36.7897C26.7523 36.7897 25.5543 35.5917 25.5543 34.1138C25.5543 32.636 26.7523 31.4379 28.2301 31.4379ZM21.9843 40.946C23.4622 40.946 24.6602 42.144 24.6602 43.6218C24.6602 45.0997 23.4622 46.2977 21.9843 46.2977C20.5065 46.2977 19.3085 45.0997 19.3085 43.6218C19.3085 42.144 20.5065 40.946 21.9843 40.946ZM27.8501 56.0515C29.328 56.0515 30.526 57.2496 30.526 58.7274C30.526 60.2053 29.328 61.4033 27.8501 61.4033C26.3723 61.4033 25.1743 60.2053 25.1743 58.7274C25.1744 57.2496 26.3723 56.0515 27.8501 56.0515ZM42.9396 42.0129C44.4174 42.0129 45.6154 43.211 45.6154 44.6888C45.6154 46.1666 44.4174 47.3647 42.9396 47.3647C41.4617 47.3647 40.2637 46.1666 40.2637 44.6888C40.2638 43.2108 41.4619 42.0129 42.9396 42.0129Z" fill="#FFE177"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M42.8932 67.019C44.3711 67.019 45.5691 68.217 45.5691 69.6949C45.5691 71.1727 44.3711 72.3708 42.8932 72.3708C42.7602 72.3708 42.6296 72.361 42.5018 72.3423C43.7941 72.1529 44.7863 71.0399 44.7863 69.695C44.7863 68.3502 43.7941 67.2372 42.5018 67.0478C42.6296 67.0288 42.7604 67.019 42.8932 67.019ZM42.6682 23.833C44.1461 23.833 45.3441 25.0311 45.3441 26.5089C45.3441 27.9868 44.1461 29.1848 42.6682 29.1848C42.5352 29.1848 42.4046 29.175 42.2768 29.1562C43.5691 28.9667 44.5612 27.8538 44.5612 26.5089C44.5612 25.1641 43.5691 24.0511 42.2768 23.8617C42.4046 23.843 42.5352 23.833 42.6682 23.833ZM55.245 23.8458C56.7229 23.8458 57.9209 25.0438 57.9209 26.5217C57.9209 27.9995 56.7229 29.1976 55.245 29.1976C55.112 29.1976 54.9814 29.1878 54.8536 29.1689C56.1459 28.9795 57.1379 27.8665 57.1379 26.5217C57.1379 25.1768 56.1457 24.0639 54.8536 23.8745C54.9814 23.8556 55.112 23.8458 55.245 23.8458ZM28.2301 31.4379C29.708 31.4379 30.906 32.636 30.906 34.1138C30.906 35.5917 29.708 36.7897 28.2301 36.7897C28.0971 36.7897 27.9665 36.7799 27.8387 36.7612C29.131 36.5718 30.1232 35.4588 30.1232 34.114C30.1232 32.7691 29.131 31.6561 27.8387 31.4667C27.9665 31.4479 28.0971 31.4379 28.2301 31.4379ZM21.9843 40.946C23.4622 40.946 24.6602 42.144 24.6602 43.6218C24.6602 45.0997 23.4622 46.2977 21.9843 46.2977C21.8513 46.2977 21.7206 46.2879 21.5929 46.2691C22.8852 46.0797 23.8774 44.9667 23.8774 43.6218C23.8774 42.277 22.8852 41.164 21.5929 40.9746C21.7206 40.9559 21.8513 40.946 21.9843 40.946ZM27.8501 56.0515C29.328 56.0515 30.526 57.2496 30.526 58.7274C30.526 60.2053 29.328 61.4033 27.8501 61.4033C27.7171 61.4033 27.5864 61.3935 27.4587 61.3748C28.751 61.1854 29.7432 60.0724 29.7432 58.7276C29.7432 57.3827 28.751 56.2697 27.4587 56.0803C27.5865 56.0615 27.7173 56.0515 27.8501 56.0515ZM42.9396 42.0129C44.4174 42.0129 45.6154 43.211 45.6154 44.6888C45.6154 46.1666 44.4174 47.3647 42.9396 47.3647C42.8066 47.3647 42.6759 47.3549 42.5481 47.336C43.8404 47.1466 44.8326 46.0336 44.8326 44.6888C44.8326 43.344 43.8404 42.231 42.5481 42.0416C42.6759 42.0227 42.8067 42.0129 42.9396 42.0129Z" fill="#FFD064"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M44.3818 69.6946C44.3818 68.8736 43.7138 68.2058 42.8929 68.2058C42.0727 68.2058 41.4047 68.8736 41.4047 69.6946C41.4047 70.5154 42.0727 71.1834 42.8929 71.1834C43.7138 71.1834 44.3818 70.5156 44.3818 69.6946ZM29.0381 68.5071V62.4032C30.5878 61.9 31.7134 60.4422 31.7134 58.7264C31.7134 57.0105 30.5878 55.5528 29.0381 55.0512V45.8762H39.2639C39.6441 47.0488 40.5705 47.9782 41.7429 48.361L41.7114 66.016C40.5334 66.3962 39.5993 67.3282 39.2178 68.5069H36.3455V52.6939C36.3455 52.0378 35.8138 51.5064 35.1585 51.5064C34.5016 51.5064 33.9707 52.0378 33.9707 52.6939V68.5069H29.0381V68.5071ZM26.3622 58.7264C26.3622 59.5474 27.0294 60.2152 27.8504 60.2152C28.67 60.2152 29.3379 59.5474 29.3379 58.7264C29.3379 57.907 28.67 57.2389 27.8504 57.2389C27.0293 57.239 26.3622 57.9072 26.3622 58.7264ZM28.2304 35.6016C29.05 35.6016 29.7179 34.9335 29.7179 34.1143C29.7179 33.2933 29.05 32.6254 28.2304 32.6254C27.4102 32.6254 26.7416 33.2933 26.7416 34.1143C26.7415 34.9335 27.4102 35.6016 28.2304 35.6016ZM26.6632 49.66V37.6438C25.3107 37.0412 24.3666 35.6858 24.3666 34.1141C24.3666 31.9826 26.0987 30.2504 28.2303 30.2504C30.3605 30.2504 32.0926 31.9827 32.0926 34.1141C32.0926 35.9665 30.7806 37.5191 29.0379 37.8918V43.5013H33.9707V29.6328C32.4671 29.3402 31.0761 28.4928 29.9847 27.2012C26.2488 27.7401 23.255 28.7672 23.2403 31.9558L23.1997 39.9551C24.7361 40.4658 25.8464 41.9157 25.8464 43.6212C25.8464 45.2097 24.8836 46.5768 23.51 47.169C24.0642 48.4233 25.2442 49.3631 26.6632 49.66ZM20.4954 43.6214C20.4954 42.8007 21.1633 42.1327 21.9842 42.1327C22.805 42.1327 23.4717 42.8008 23.4717 43.6214C23.4717 44.4422 22.8052 45.1105 21.9842 45.1105C21.1632 45.1105 20.4954 44.4422 20.4954 43.6214ZM33.1246 24.6512C33.7729 24.8679 34.4549 24.9867 35.1585 24.9867C35.8621 24.9867 36.5432 24.8679 37.1916 24.6512V25.7779C37.1916 26.0912 37.3145 26.3777 37.5151 26.5914C36.7939 27.0975 35.985 27.3737 35.1585 27.3737C34.3284 27.3737 33.5166 27.0961 32.7934 26.5868C32.9981 26.3731 33.1246 26.0822 33.1246 25.7661V24.6512ZM35.1585 22.6117C37.8539 22.6117 40.2022 19.7752 40.5879 16.1088L39.4867 13.2126C38.065 13.5704 36.2875 13.6386 34.4179 13.3952C33.2288 13.241 32.1081 12.9722 31.1146 12.61L29.7285 16.1162C30.1175 19.7795 32.4643 22.6117 35.1585 22.6117ZM28.4233 10.5837C28.2353 9.81623 28.3409 9.14841 28.7293 8.65248C29.1779 8.07966 29.9897 7.74998 30.956 7.74998H31.4193C32.0753 7.74998 32.6064 7.21858 32.6064 6.56248C32.6064 6.32216 32.6644 6.14983 32.7 6.09802C32.7147 6.09505 32.7524 6.08629 32.8188 6.08629H38.6766C39.5506 6.08629 40.7516 5.79669 41.6242 4.99958C41.9079 5.8249 42.1839 6.922 42.325 8.22528C42.4528 9.41575 42.5193 11.3186 41.975 13.0718L41.3021 11.3024C41.1847 10.9965 40.9486 10.753 40.646 10.6283C40.5007 10.5675 40.3463 10.5379 40.1918 10.5379C40.0256 10.5379 39.8607 10.5721 39.7063 10.6417C38.5891 11.1419 36.6796 11.2951 34.7247 11.0397C33.3147 10.8571 31.9895 10.4786 30.9932 9.97699C30.6948 9.82677 30.3476 9.80911 30.0359 9.92786C29.7243 10.0466 29.4776 10.2917 29.3547 10.6018L28.7832 12.0477L28.4233 10.5837ZM41.1804 26.5082C41.1804 27.3292 41.8469 27.9969 42.6679 27.9969C43.4882 27.9969 44.1567 27.329 44.1567 26.5082C44.1567 25.6875 43.488 25.0207 42.6679 25.0207C41.8469 25.0207 41.1804 25.6875 41.1804 26.5082ZM46.4792 27.139C46.1767 28.9706 44.5836 30.3719 42.6679 30.3719C41.1727 30.3719 39.8754 29.5183 39.2325 28.2731C38.3641 28.9663 37.3818 29.4308 36.3455 29.6328V43.5013H39.2639C39.6454 42.3227 40.5775 41.3905 41.7561 41.0105L41.7693 33.032C41.7708 32.3772 42.3023 31.8475 42.9571 31.8475H42.9599C44.977 31.8475 48.3837 30.2975 51.6479 27.9302C51.4774 27.4938 51.381 27.0187 51.381 26.5214C51.381 24.3913 53.1145 22.6577 55.2447 22.6577C55.8085 22.6577 56.3445 22.7808 56.8286 22.9991C58.3321 21.0529 58.7876 19.7437 58.6842 19.1368C58.657 18.9852 58.5933 18.8576 58.369 18.7272C57.3224 18.117 56.8829 18.4229 56.4916 18.8206C55.9586 19.3611 55.415 19.9489 54.8407 20.5708C52.5123 23.0911 49.8964 25.9202 46.4792 27.139ZM56.7337 26.5215C56.7337 27.3425 56.0657 28.0104 55.2449 28.0104C54.4239 28.0104 53.756 27.3425 53.756 26.5215C53.756 25.7005 54.424 25.0329 55.2449 25.0329C56.0657 25.0327 56.7337 25.7005 56.7337 26.5215ZM44.4278 44.6888C44.4278 43.8679 43.7598 43.2 42.939 43.2C42.118 43.2 41.4509 43.8678 41.4509 44.6888C41.4509 45.5098 42.1181 46.1761 42.939 46.1761C43.76 46.1761 44.4278 45.5097 44.4278 44.6888ZM44.1176 48.3672L44.0868 66.0209C45.635 66.5256 46.7572 67.9801 46.7572 69.6947C46.7572 71.8245 45.0232 73.5584 42.8928 73.5584C41.1775 73.5584 39.7194 72.4331 39.2178 70.8821H27.8503C27.1942 70.8821 26.6632 70.3507 26.6632 69.6946V62.4032C25.1115 61.9 23.9866 60.4422 23.9866 58.7264C23.9866 57.0105 25.1115 55.5528 26.6632 55.0512V52.0691C24.0075 51.7025 21.7955 49.8486 21.0591 47.3724C19.3732 46.9571 18.1205 45.4325 18.1205 43.6214C18.1205 41.8952 19.2593 40.4301 20.8252 39.9358L20.865 31.944C20.8783 29.2142 22.2652 27.2268 24.9871 26.0317C26.7876 25.2422 28.9444 24.9111 30.7497 24.7017V23.2886C28.8996 21.7079 27.6098 19.1516 27.3457 16.1504L26.1168 11.151C25.7529 9.67106 26.0177 8.26239 26.8602 7.1877C27.6665 6.15903 28.9429 5.52238 30.4186 5.39888C30.7833 4.35536 31.658 3.71115 32.8185 3.71115H38.6763C39.1304 3.71115 39.7578 3.53154 40.0806 3.18716C40.2022 3.05787 40.3385 2.85733 40.3133 2.44928C40.2839 1.99239 40.5214 1.56058 40.9204 1.33778C41.3207 1.11497 41.8125 1.14214 42.1864 1.40769C43.416 2.28169 44.2943 5.06786 44.6212 7.44316C44.9132 9.57472 45.0677 13.5067 42.945 16.3999C42.6335 19.2928 41.364 21.7525 39.5669 23.2887V24.2075C40.2718 23.2605 41.3995 22.646 42.6676 22.646C44.1608 22.646 45.4568 23.4967 46.101 24.739C48.7916 23.6153 51.0644 21.1588 53.0948 18.9586C53.6845 18.322 54.24 17.7207 54.8024 17.1523C56.1159 15.821 57.8081 15.6515 59.5653 16.6743C60.3688 17.1436 60.8732 17.8558 61.0234 18.736C61.2833 20.2471 60.4638 22.2168 58.592 24.5978C58.9197 25.165 59.1083 25.8211 59.1083 26.5215C59.1083 28.6518 57.3748 30.3852 55.2446 30.3852C54.476 30.3852 53.7599 30.1581 53.1575 29.7693C50.4621 31.7376 47.0001 33.6704 44.1432 34.1229L44.1306 41.0136C45.6788 41.5183 46.8031 42.9744 46.8031 44.6888C46.8034 46.4076 45.6736 47.8683 44.1176 48.3672ZM67.3228 1.18741H56.3089C55.6528 1.18741 55.1211 1.71911 55.1211 2.37521C55.1211 3.0313 55.6528 3.56301 56.3089 3.56301H66.1357V13.3894C66.1357 14.0455 66.6667 14.5769 67.3228 14.5769C67.9796 14.5769 68.5106 14.0455 68.5106 13.3894V2.37521C68.5106 1.71911 67.9795 1.18741 67.3228 1.18741ZM67.3228 61.4236C66.6667 61.4236 66.1357 61.9551 66.1357 62.6111V72.4377H56.3089C55.6528 72.4377 55.1211 72.9691 55.1211 73.6252C55.1211 74.2813 55.6528 74.8127 56.3089 74.8127H67.3228C67.9796 74.8127 68.5106 74.2813 68.5106 73.6252V62.6111C68.5106 61.9552 67.9795 61.4236 67.3228 61.4236ZM19.6911 72.4377H9.86426V62.6111C9.86426 61.9551 9.33256 61.4236 8.67721 61.4236C8.02111 61.4236 7.48941 61.9551 7.48941 62.6111V73.6252C7.48941 74.2813 8.02111 74.8127 8.67721 74.8127H19.6911C20.3472 74.8127 20.8782 74.2813 20.8782 73.6252C20.8782 72.9691 20.3472 72.4377 19.6911 72.4377ZM7.48941 13.3894C7.48941 14.0455 8.02111 14.5769 8.67721 14.5769C9.33256 14.5769 9.86426 14.0455 9.86426 13.3894V3.56286H19.6911C20.3472 3.56286 20.8782 3.03115 20.8782 2.37506C20.8782 1.71897 20.3472 1.18726 19.6911 1.18726H8.67721C8.02111 1.18726 7.48941 1.71897 7.48941 2.37506V13.3894Z" fill="black"/>
</svg>
					</li>
					<li class="list-inline-item">
						<svg width="78" height="78" viewBox="0 0 78 78" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M62.4179 1.7015H1.5224V61.0746H62.4179V1.7015Z" fill="white"/>
<path d="M62.4179 1.7015H1.5224V61.0746H62.4179V1.7015Z" fill="white"/>
<path d="M1.5224 1.7015H62.4179V15.403H25.4533L20.1758 14.3078L1.5224 15.403V1.7015Z" fill="#BC9AF4"/>
<path d="M24.3689 26.7445C24.3689 17.6229 26.8219 9.07092 31.1072 1.7015H1.5224V61.0746H38.0597C29.571 52.102 24.3689 40.0273 24.3689 26.7445Z" fill="#D2DCFD"/>
<path d="M31.209 1.7015H1.5224V15.403H25.8239C26.969 10.5296 28.7991 5.92529 31.209 1.7015Z" fill="#6864F7"/>
<path d="M54.0448 52.7015H31.2331L21.8728 51.3289L11.194 51.6719L11.3131 41.2702L10.6567 24.4959L19.875 25.4389L24.1939 23.7761H54.0448V52.7015Z" fill="#FDCB50"/>
<path d="M24.0619 26.8967C24.0619 25.8486 24.0955 24.8083 24.159 23.7761H9.89551V52.7015H31.2089C26.6733 45.1625 24.0619 36.3354 24.0619 26.8967Z" fill="#FD8F01"/>
<path d="M55.9478 49.6567C46.8522 49.6567 39.0569 55.1575 35.7761 62.9776C39.0568 70.7977 46.852 76.2985 55.9478 76.2985C65.0435 76.2985 72.8386 70.7977 76.1194 62.9776C72.8388 55.1575 65.0435 49.6567 55.9478 49.6567Z" fill="white"/>
<path d="M55.9477 69.4478C59.5211 69.4478 62.4179 66.551 62.4179 62.9776C62.4179 59.4042 59.5211 56.5075 55.9477 56.5075C52.3744 56.5075 49.4776 59.4042 49.4776 62.9776C49.4776 66.551 52.3744 69.4478 55.9477 69.4478Z" fill="#B1D952"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M0 1.7015C0 0.860704 0.678366 0.179108 1.51517 0.179108H62.4251C63.2619 0.179108 63.9403 0.860704 63.9403 1.7015V50.3946H60.91V3.22388H3.03035V59.5522H36.5592V62.597H1.51517C0.678366 62.597 0 61.9154 0 61.0746V1.7015Z" fill="#052A75"/>
<path d="M10.6567 8.55224C10.6567 9.39303 9.97512 10.0746 9.13433 10.0746C8.29353 10.0746 7.61194 9.39303 7.61194 8.55224C7.61194 7.71145 8.29353 7.02985 9.13433 7.02985C9.97512 7.02985 10.6567 7.71145 10.6567 8.55224Z" fill="white"/>
<path d="M17.5075 8.55224C17.5075 9.39303 16.8259 10.0746 15.9851 10.0746C15.1443 10.0746 14.4627 9.39303 14.4627 8.55224C14.4627 7.71145 15.1443 7.02985 15.9851 7.02985C16.8259 7.02985 17.5075 7.71145 17.5075 8.55224Z" fill="white"/>
<path d="M23.597 8.55224C23.597 9.39303 22.9154 10.0746 22.0746 10.0746C21.2338 10.0746 20.5522 9.39303 20.5522 8.55224C20.5522 7.71145 21.2338 7.02985 22.0746 7.02985C22.9154 7.02985 23.597 7.71145 23.597 8.55224Z" fill="white"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M31.209 8.55224C31.209 7.71145 31.8917 7.02985 32.7338 7.02985H55.5647C56.4068 7.02985 57.0896 7.71145 57.0896 8.55224C57.0896 9.39303 56.4068 10.0746 55.5647 10.0746H32.7338C31.8917 10.0746 31.209 9.39303 31.209 8.55224Z" fill="white"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M28.9432 35.2272L25.0371 45.6129C24.7361 46.4131 23.8515 46.8148 23.0612 46.51C22.271 46.2052 21.8743 45.3094 22.1753 44.5091L27.2349 31.0565C27.2393 31.0448 27.2439 31.0332 27.2485 31.0216C27.8705 29.4811 30.0221 29.4811 30.6468 31.0174C30.6526 31.0316 30.6582 31.0459 30.6635 31.0603L35.6771 44.5135C35.9757 45.3147 35.5763 46.2093 34.7851 46.5117C33.9939 46.814 33.1105 46.4096 32.812 45.6084L28.9432 35.2272Z" fill="#052A75"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M23.597 42.0448C23.597 41.204 24.2881 40.5224 25.1407 40.5224H32.71C33.5626 40.5224 34.2537 41.204 34.2537 42.0448C34.2537 42.8856 33.5626 43.5672 32.71 43.5672H25.1407C24.2881 43.5672 23.597 42.8856 23.597 42.0448Z" fill="#052A75"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M41.1045 29.8657C41.9453 29.8657 42.6269 30.5599 42.6269 31.4163V45.0614C42.6269 45.9177 41.9453 46.6119 41.1045 46.6119C40.2637 46.6119 39.5821 45.9177 39.5821 45.0614V31.4163C39.5821 30.5599 40.2637 29.8657 41.1045 29.8657Z" fill="#052A75"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M34.3705 62.3973C37.8787 54.0269 46.2155 48.1343 55.9478 48.1343C65.6801 48.1343 74.0169 54.0269 77.525 62.3973C77.6807 62.7688 77.6807 63.1864 77.525 63.558C74.0168 71.9283 65.6801 77.8209 55.9478 77.8209C46.2154 77.8209 37.8786 71.9283 34.3705 63.5579C34.2148 63.1864 34.2148 62.7688 34.3705 62.3973ZM37.4518 62.9776C40.6375 69.9467 47.7222 74.7917 55.9478 74.7917C64.1733 74.7917 71.2579 69.9467 74.4437 62.9776C71.258 56.0085 64.1733 51.1636 55.9478 51.1636C47.7224 51.1636 40.6376 56.0085 37.4518 62.9776Z" fill="#052A75"/>
</svg>
					</li>
				
     	<li class="list-inline-item">
						<svg width="98" height="98" viewBox="0 0 98 98" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M65.0558 39.0469L49.1418 31.2586L33.2277 39.0469L49.1418 46.8087L65.0558 39.0469Z" fill="#FFBA33"/>
<path d="M65.0558 39.0469L49.1418 46.8185V68.9062L65.0558 60.8346V39.0469Z" fill="#027EF1"/>
<path d="M33.2277 39.0469L49.1418 46.8185V68.9062L33.2277 60.8346V39.0469Z" fill="#0048D4"/>
<path fill-rule="evenodd" clip-rule="evenodd" d="M12.7668 32.1562C12.7668 21.1623 21.5882 12.25 32.4699 12.25H40.8058C42.4799 12.25 43.8371 13.6212 43.8371 15.3125C43.8371 17.0038 42.4799 18.375 40.8058 18.375H32.4699C24.9363 18.375 18.8293 24.545 18.8293 32.1562V40.5781C18.8293 42.2695 17.4721 43.6406 15.798 43.6406C14.124 43.6406 12.7668 42.2695 12.7668 40.5781V32.1562ZM54.4465 15.3125C54.4465 13.6212 55.8036 12.25 57.4777 12.25H65.8137C76.6951 12.25 85.5168 21.1623 85.5168 32.1562V40.5781C85.5168 42.2695 84.1595 43.6406 82.4855 43.6406C80.8115 43.6406 79.4543 42.2695 79.4543 40.5781V32.1562C79.4543 24.545 73.3472 18.375 65.8137 18.375H57.4777C55.8036 18.375 54.4465 17.0038 54.4465 15.3125ZM15.798 54.3594C17.4721 54.3594 18.8293 55.7305 18.8293 57.4219V65.8438C18.8293 73.455 24.9363 79.625 32.4699 79.625H40.8058C42.4799 79.625 43.8371 80.9962 43.8371 82.6875C43.8371 84.3788 42.4799 85.75 40.8058 85.75H32.4699C21.5882 85.75 12.7668 76.8374 12.7668 65.8438V57.4219C12.7668 55.7305 14.124 54.3594 15.798 54.3594ZM82.4855 54.3594C84.1595 54.3594 85.5168 55.7305 85.5168 57.4219V65.8438C85.5168 76.8374 76.6951 85.75 65.8137 85.75H57.4777C55.8036 85.75 54.4465 84.3788 54.4465 82.6875C54.4465 80.9962 55.8036 79.625 57.4777 79.625H65.8137C73.3472 79.625 79.4543 73.455 79.4543 65.8438V57.4219C79.4543 55.7305 80.8115 54.3594 82.4855 54.3594Z" fill="#FFBA33"/>
</svg>
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
    height=1100,
)
