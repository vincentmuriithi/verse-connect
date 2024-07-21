$(() => {
    var suppliers0 = $("#suppliers0"); 
    var suppliers1 = $("#suppliers1");
    var proceed_btn = $("#proceed_btn");
    let checkbox = $("#mycheckbox");
    let notChecked = $("#notchecked");
    let suppliers = document.getElementsByName("supplier");
    suppliers1.hide();

    $(document).click((event) => {
        if (!$(event.target).closest(".suppliers1").length)
            suppliers1.hide();
    })
    const payment_redirect = async () => {
        let result = await fetch("/payment_redirect", {
            method: "get"

        });
        if (result.redirected)
            window.location.href = result.url;
        else
            return await result.text();
    };

    suppliers0.on("click", () => {
        suppliers1.toggle();
        if (suppliers0.text() == "view")
            suppliers0.text("clear");
        else
            suppliers0.text("view");
    });

    proceed_btn.on("click", () => {
        let presence = false;
        let name = "";
        suppliers.forEach((k) => {
            if (k.checked) {
                presence = true;
                name = k.value;
            }
        })
        if (checkbox.is(":checked") && presence){ 
            notChecked.text("");
            payment_redirect()
                .then(() => {})
                .catch((err) => console.error(err));   
        }
        else {
            if (!presence)
                    notChecked.text("Choose a supplier");
                else
                    notChecked.text("You need to confirm payment before proceed")
        }
    })

});