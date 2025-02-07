//"gender", "age", "height", "weight", "duration", "heart_rate", "body_temp"
  function getGenderValue() {
    var uiGender = document.getElementsByName("uiGender");
    for(var i in uiGender) {
      if(uiGender[i].checked) {
          return parseInt(i)+1;
      }
    }
    return -1; // Invalid Value
  }
  
  function onClickedEstimateCalories() {
    console.log("Estimate calories button clicked");
    var gender = getGenderValue();
    var age = document.getElementById("uiAge");
    var height = document.getElementById("uiHeight");
    var weight = document.getElementById("uiWeight");
    var duration = document.getElementById("uiDuration");
    var heart_rate = document.getElementById("uiHeart_rate");
    var body_temp = document.getElementById("uiBody_temp");
    var estCalories = document.getElementById("uiEstimatedCalories");
  
    var url = "http://127.0.0.1:5000/predict_calories_burnt"; //Use this if you are NOT using nginx which is first 7 tutorials
    //var url = "/api/predict_home_price"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
  
    $.post(url, {
        gender: gender,
        age: parseInt(age.value),
        height: parseFloat(height.value),
        weight: parseFloat(weight.value),
        duration: parseFloat(duration.value),
        heart_rate: parseFloat(heart_rate.value),
        body_temp: parseFloat(body_temp.value)
    },function(data, status) {
        console.log(data.estimated_calories_burnt);
        estCalories.innerHTML = "<h2>" + data.estimated_calories_burnt.toString() + " Cal</h2>";
        console.log(status);
    });
  }
  