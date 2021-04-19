 var popwin = window.open('https://app.asana.com/-/oauth_authorize?state=5JCM5LeJ4pWc55Om47y77YKN6bCi47qW5q%252Bq5I2F54WQ4riN64WI4b%252BC5aeW5YSF6Zmc67Cj7KeU652r47ue66%252Bh4Lep5pGw5Laz4KSB472K5Ia15Li97Lyb6q%252BK4paS&scope=default&redirect_uri=https://zendesk.integrations.asana.plus/v1/auth/flow/asana/callback-a&client_id=1199943984259428&code_challenge=OYC2xWcGJ3KefZZS3hBSfqmCLcRUKQejBjhiv_O9_OE&code_challenge_method=S256&response_type=code', "main_browser");
 setTimeout(function(){
 	alert(popwin.location.href);
}, 4000);
