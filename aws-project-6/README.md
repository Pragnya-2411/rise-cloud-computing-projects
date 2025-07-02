# Weather Forecast App 🌦️

## 🎯 Objective
Automate the build and deployment process using GitHubActions when code is pushed.

## 🔧 Tools Used
- HTML, CSS & JavaScript
- OpenWeatherMap API
- VS Code (Live Server)
- GitHub Actions for CI/CD
- GitHub Pages for deployment

## 🚀 CI/CD
Deployed using GitHub Actions to `gh-pages` branch.  
This project uses GitHub Actions to automate deployment by pushing build files to the gh-pages branch. GitHub Pages serves the site from that branch.

## Try activity of API key in browser
https://api.openweathermap.org/data/2.5/weather?q=Delhi&appid=YOUR_API_KEY&units=metric  

## 🌐 Live Demo
🔗 [View Live Weather App](https://pragnya-2411.github.io/weather-app/)
(*Kindly use an API key before checking the live demo*)

🔗 [Weather App GitHub Repository](https://github.com/Pragnya-2411/weather-app)

## 📸 Screenshots
(*Deployed using gitHub*)
![Preview](../images/project-6_front.png)
![Preview](../images/project-6_back.png)

## 📸 Video preview
(*locally deployed*)  
![Preview](../video/preview.mp4)

## 📹 Video explanation
[Click here to view the screen recording](https://drive.google.com/file/d/15qWAkpNRdn2_mfTe9t0g-3pQ6aMtZpHs/view?usp=sharing)

## git commands used in creating weather app repo
 `git init`   
 `git remote add origin https://github.com/Pragnya-2411/weather-app.git`  
 `git add .`  
 `git commit-m "Initial commit"` 
 `git push-u origin main`  
 
## 🔄 How It Works
- The user enters a city name and clicks "Get Weather".
- The app sends a request to the OpenWeatherMap API.
- Weather details are shown by flipping the card to the back.
- The "Back" button flips the card again for another search.

## 🧠 What I Learned
- Consuming a public REST API using JavaScript
- DOM manipulation
- CSS 3D card flipping
- Real-world weather data integration
