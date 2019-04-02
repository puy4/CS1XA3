function chBackcolor(color) {
    document.body.style.background = color;

}


function caloriescalcappear(){
    document.getElementById("bkg").style.display = "none";
    document.getElementById("calc").innerHTML = ""
    document.getElementById('entry').type = 'hidden';
    document.getElementById('v1').type = 'hidden';
    document.getElementById('v2').type = 'hidden';
    document.getElementById('v3').type = 'hidden';
    document.getElementById('v4').type = 'hidden';
    document.getElementById('v5').type = 'hidden';
    document.getElementById('v6').type = 'hidden';
    document.getElementById('v7').type = 'hidden';
    document.getElementById('v8').type = 'hidden';
    document.getElementById('v9').type = 'hidden';
    document.getElementById('v0').type = 'hidden';
    document.getElementById('s1').type = 'hidden';
    document.getElementById('s2').type = 'hidden';
    document.getElementById('s3').type = 'hidden';
    document.getElementById('s4').type = 'hidden';
    document.getElementById('s5').type = 'hidden';
    document.getElementById('s6').type = 'hidden';

    document.getElementById('wo1').type = 'checkbox';
    document.getElementById('wo2').type = 'checkbox';
    document.getElementById('wo3').type = 'checkbox';
    document.getElementById('wo4').type = 'checkbox';
    document.getElementById('wo5').type = 'checkbox';
    document.getElementById("workout").style.display = "inline";
    document.getElementById("sexes").style.display = "inline";
    document.getElementById('age').type = 'text';
    document.getElementById('female').type = 'checkbox';
    document.getElementById('male').type = 'checkbox';
    document.getElementById('weight').type = 'text';
    document.getElementById('height').type = 'text';
    document.getElementById('bo').type = 'button';
    document.getElementById("agetag").innerHTML = "Age:";
    document.getElementById("sextag").innerHTML = "Sex:";

    document.getElementById("weighttag").innerHTML = "Weight(in kg):";
    document.getElementById("heighttag").innerHTML = "height(in cm):";
    document.getElementById("calc").innerHTML = "Calories Intake Calculator";

}
function calculatorappears(){
    document.getElementById("bkg").style.display = "inline";
    document.getElementById("calc").innerHTML = "Calculator";
    document.getElementById('entry').type = 'text';
    document.getElementById('v1').type = 'button';
    document.getElementById('v2').type = 'button';
    document.getElementById('v3').type = 'button';
    document.getElementById('v4').type = 'button';
    document.getElementById('v5').type = 'button';
    document.getElementById('v6').type = 'button';
    document.getElementById('v7').type = 'button';
    document.getElementById('v8').type = 'button';
    document.getElementById('v9').type = 'button';
    document.getElementById('v0').type = 'button';
    document.getElementById('s1').type = 'button';
    document.getElementById('s2').type = 'button';
    document.getElementById('s3').type = 'button';
    document.getElementById('s4').type = 'button';
    document.getElementById('s5').type = 'button';
    document.getElementById('s6').type = 'button';
    document.getElementById("workout").style.display = "none"
    document.getElementById("sexes").style.display = "none"
    document.getElementById('age').type = 'hidden';
    document.getElementById('female').type = 'hidden';
    document.getElementById('male').type = 'hidden';
    document.getElementById('weight').type = 'hidden';
    document.getElementById('height').type = 'hidden';
    document.getElementById('bo').type = 'hidden';
    document.getElementById("agetag").innerHTML = '';
    document.getElementById("sextag").innerHTML = '';
    document.getElementById("femaletag").innerHTML = '';
    document.getElementById("maletag").innerHTML = '';
    document.getElementById("weighttag").innerHTML = '';
    document.getElementById("heighttag").innerHTML = '';

}



function validation(){
    var colour = 'rgb(' + (Math.floor(Math.random() * 256)) + ',' + (Math.floor(Math.random() * 256)) + ',' + (Math.floor(Math.random() * 256)) + ')';
    chBackcolor(colour);
    
    var ageinput = parseInt(document.getElementById("age").value);
    var femaleinput = document.getElementById("female");
    var maleinput = document.getElementById("male");
    var heightinput = parseInt(document.getElementById("height").value);
    var weightinput = parseInt(document. getElementById("weight").value);
    var noworkout=document.getElementById("wo1");
    var someworkout=document.getElementById("wo2");
    var moreworkout=document.getElementById("wo3");
    var alotworkout=document.getElementById("wo4");
    var extremeworkout=document.getElementById("wo5");
    var msg;

    
    if ( ageinput > 140 || ageinput <= 0){
        msg = "Please consult with a specialist";
    } else if (heightinput <=0 || heightinput >250){
        msg = "Please consult with a specialist"
    } else if (weightinput > 500 || weightinput <=0){
        msg = "Please consult with a specialist"
    } else if (ageinput > 0 && ageinput < 18){
        msg = "Please consult with a specialist"
    } else if (femaleinput.checked == true && maleinput.checked == true ){
        msg = "Please consult with a specialist"
    }
      else if (noworkout.checked==true && ageinput >= 18 && ageinput <= 140 && femaleinput.checked == true && heightinput > 0 && heightinput<=250 && weightinput >0 && weightinput<500){
        msg = (655 + (9.6 * weightinput) + (1.8 * heightinput) - (4.7 * ageinput))*1.2       
    } else if (someworkout.checked==true && ageinput >= 18 && ageinput <= 140 && femaleinput.checked == true && heightinput > 0 && heightinput<=250 && weightinput >0 && weightinput<500){
        msg = (655 + (9.6 * weightinput) + (1.8 * heightinput) - (4.7 * ageinput))*1.375
    } else if (moreworkout.checked==true && ageinput >= 18 && ageinput <= 140 && femaleinput.checked == true && heightinput > 0 && heightinput<=250 && weightinput >0 && weightinput<500){
        msg = (655 + (9.6 * weightinput) + (1.8 * heightinput) - (4.7 * ageinput))*1.55
    } else if (alotworkout.checked==true && ageinput >= 18 && ageinput <= 140 && femaleinput.checked == true && heightinput > 0 && heightinput<=250 && weightinput >0 && weightinput<500){
        msg = (655 + (9.6 * weightinput) + (1.8 * heightinput) - (4.7 * ageinput))*1.725
    } else if (extremeworkout.checked==true && ageinput >= 18 && ageinput <= 140 && femaleinput.checked == true && heightinput > 0 && heightinput<=250 && weightinput >0 && weightinput<500){
        msg = (655 + (9.6 * weightinput) + (1.8 * heightinput) - (4.7 * ageinput))*1.9
    } else if (noworkout.checked==true && ageinput >= 18 && ageinput <= 140 && maleinput.checked == true && heightinput > 0 && heightinput<=250 && weightinput >0 && weightinput<500){
        msg = (66 + (13.7 * weightinput) + (5 * heightinput) - (6.8*ageinput))*1.2
    } else if (someworkout.checked==true && ageinput >= 18 && ageinput <= 140 && maleinput.checked == true && heightinput > 0 && heightinput<=250 && weightinput >0 && weightinput<500){
        msg = (66 + (13.7 * weightinput) + (5 * heightinput) - (6.8*ageinput))*1.375
    }else if (moreworkout.checked==true && ageinput >= 18 && ageinput <= 140 && maleinput.checked == true && heightinput > 0 && heightinput<=250 && weightinput >0 && weightinput<500){
        msg = (66 + (13.7 * weightinput) + (5 * heightinput) - (6.8*ageinput))*1.55
    }else if (alotworkout.checked==true && ageinput >= 18 && ageinput <= 140 && maleinput.checked == true && heightinput > 0 && heightinput<=250 && weightinput >0 && weightinput<500){
        msg = (66 + (13.7 * weightinput) + (5 * heightinput) - (6.8*ageinput))*1.725
    }else if (extremeworkout.checked==true && ageinput >= 18 && ageinput <= 140 && maleinput.checked == true && heightinput > 0 && heightinput<=250 && weightinput >0 && weightinput<500){
        msg = (66 + (13.7 * weightinput) + (5 * heightinput) - (6.8*ageinput))*1.9
    }else {
        msg = "please check your entry"
    }


    document.getElementById("div1").innerHTML = msg;



  
  
}
function clear(){
    document.getElementById('entry').value= "";
}
  

function num(value){
    document.getElementById('entry').value+=value;
}
function cal(){
    document.getElementById('entry').value = eval(document.getElementById('entry').value);
}





