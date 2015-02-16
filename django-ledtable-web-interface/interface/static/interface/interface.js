function setColorPickerRGB(rgbString, picker) {
    var splitString = rgbString.split(',');
    var rgb = {
        r: parseInt(splitString[0].substring(1)),
        g: parseInt(splitString[1]),
        b: parseInt(splitString[2].slice(0,-1))
    }
    picker.setRgb(rgb);
}

function initColorPicker(colorInput, previewBlock, pickerElem){

    var cp = ColorPicker(pickerElem, function(hex, hsv, rgb){
            var newVal = "("+rgb.r+","+rgb.g+","+rgb.b+")";
            $(colorInput).val(newVal);
            $(previewBlock).css("background-color", hex);
        });

    $(colorInput).change(function(){
        setColorPickerRGB($(this).val(), cp);
    });
    $(colorInput).keypress(function(e){
        if(e.which == 13){
            e.preventDefault();
            e.stopImmediatePropagation();
            setColorPickerRGB($(this).val(), cp);
        }
    });
    $(colorInput).val("(0,0,0)")
    setColorPickerRGB($(colorInput).val(), cp);
}

$(document).ready(function(){

    $.each($(".colorPickerOuter"), function(i, colorPickerOuter){
        var colorInput = $(colorPickerOuter).find(".colorInput")[0];
        var picker = $(colorPickerOuter).find(".pickerUi")[0];
        var previewBlock = $(colorPickerOuter).find(".previewBlock")[0];
        initColorPicker(colorInput, previewBlock, picker);
    });

    $("#addColorButton").click(function(){
        var existingColorPicker = $(".colorPickerOuter")[0];
        var newColorPicker = $(existingColorPicker).clone();
        $("#colorListOuter").append(newColorPicker);

        var newColorInput = $(newColorPicker).find(".colorInput")[0];
        var newPreviewBlock = $(newColorPicker).find(".previewBlock")[0];
        var newPicker = $(newColorPicker).find(".pickerUi")[0];
        initColorPicker(newColorInput, newPreviewBlock, newPicker);

    });

});