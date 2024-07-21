$(() => {
    let pic_form = $("#pic_form");
    pic_form.hide();
    var profile_btn = $("#profile_btn");
    $(".menu").hide();
    var menu_bar = $("#menu_bar");
    menu_bar.on("click", () => {
        $(".menu").toggle();
    })
    $(document).click((event) => {
        if (!$(event.target).closest(".dropdown").length) {
            $(".menu").hide();
        }

        if (!$(event.target).closest(".pic_listener").length)
            pic_form.hide();
    })
    profile_btn.click(() => {
        pic_form.toggle();
    })
})