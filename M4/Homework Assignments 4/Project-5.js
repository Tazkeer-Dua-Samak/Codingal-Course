var personalInfo = ["Name: Tinu", "Age: 5", "Hobby: Reading", "Favorite Sport: Roller Skating", "Grade: LKG (Lower Kindergarten)"];
var favColors = ["Violet", "Indigo", "Blue", "Green", "Yellow", "Orange","Red"];

document.getElementById("info").innerHTML = personalInfo.join("<br>");
favColors.pop();
document.getElementById("colors").innerHTML = "My favorite colors are " + favColors.join(", ") + " and Red.";

document.getElementById("color2").innerHTML = "My friend's favorite color is " + favColors[5];

    