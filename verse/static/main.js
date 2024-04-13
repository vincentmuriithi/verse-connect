$(() => {
    var k = 0;
    var cont = $("#container");
    var img = $("#mainpic");
    $("#page").hide();
    const fade = () => {
        let word = $("#karibu");
        word.fadeToggle(4000, ()=> fade());
    };
    $("#main").on("click", () => {
        let url = $("#page").attr("href");
        window.location.href = url;
    });
    fade();
    image_array = [
        "static/images/dress7.jpg",
        "static/images/dress8.jpg",
        "static/images/dress9.jpg",
        "static/images/suit1.jpg",
        "static/images/suit2.jpg",
       "static/images/suit3.jpg",
    ];
    const slider = () => {
        img.attr("src", image_array[k])
       k = (k + 1) % image_array.length; 
    };
    setInterval(slider, 6000);
});