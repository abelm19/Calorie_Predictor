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

  // Validation for the inputs
  if (!gender || !age.value || !height.value || !weight.value || !duration.value || !heart_rate.value || !body_temp.value) {
      alert("Please fill in all fields");
      return;
  }

  // Make sure to parse and validate numbers
  age = parseInt(age.value);
  height = parseFloat(height.value);
  weight = parseFloat(weight.value);
  duration = parseFloat(duration.value);
  heart_rate = parseFloat(heart_rate.value);
  body_temp = parseFloat(body_temp.value);

  if (isNaN(age) || isNaN(height) || isNaN(weight) || isNaN(duration) || isNaN(heart_rate) || isNaN(body_temp)) {
      alert("Please enter valid numeric values.");
      return;
  }

  var url = "http://127.0.0.1:5000/predict_calories_burnt"; // Replace with the correct backend URL if needed.

  // Send the POST request using jQuery
  $.post(url, {
      gender: gender,
      age: age,
      height: height,
      weight: weight,
      duration: duration,
      heart_rate: heart_rate,
      body_temp: body_temp
  }, function(data, status) {
      if (status === "success") {
          console.log("Calories burnt: " + data.estimated_calories_burnt);
          estCalories.innerHTML = "<h2>" + data.estimated_calories_burnt + " Cal</h2>";
      } else {
          alert("Error in the request.");
      }
  }).fail(function(xhr, status, error) {
      console.log("Request failed: " + error);
      alert("Failed to get data. Please try again.");
  });
}