$(() => {
    var menu_bar = $("#menu_bar");
    let menu_cont = $("#menu_cont");
    menu_cont.hide();
    menu_bar.on("click", () => {
        menu_cont.show();
    })
    $(document).on("click", (event) => {
        if (!$(event.target).closest(".menu_shop").length)
            menu_cont.hide();
    })
});



