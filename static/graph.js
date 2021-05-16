function on_load_function(shop_data){
    create_chart(shop_data)
    create_top(shop_data)
}

function create_chart(shop_data) {
    dates = []
    data_set = []
    line_color=['#5ec100','#00b4e3','#00583d','#f06c01','#00539f']
    for (i = 0; i < shop_data[0].length; i++) {
        dates.push(shop_data[0][i]['date']);
    }
    for (shop_num = 0; shop_num < shop_data.length; shop_num++) {
        prices = []
        for (i = 0; i < shop_data[0].length; i++) {
            prices.push(shop_data[shop_num][i]['price']);
        }
        var data = {
            data: prices,
            label: shop_data[shop_num][0]['shop'],
            borderColor: line_color[shop_num],
            backgroundColor: line_color[shop_num],
            fill: false,
        };
        data_set.push(data)
    }
    var option = {
    responsive:true,
    maintainAspectRatio: false
};
    const plugin = {
  id: 'custom_canvas_background_color',
  beforeDraw: (chart) => {
    const ctx = chart.canvas.getContext('2d');
    ctx.save();
    ctx.globalCompositeOperation = 'destination-over';
    ctx.fillStyle = '#EADEDA';
    ctx.fillRect(0, 0, chart.width, chart.height);
    ctx.restore();
  }
};
    var the_chart_canvas = document.getElementById('myChart').getContext('2d');
    var myChart = new Chart(the_chart_canvas, {
        type: 'line',
        data: {
            labels: dates,
            datasets: data_set
        },
        options:option,
        plugins: [plugin],
    });
}
function create_top(shop_data){
    default_prices={'asda':2.5,'coop':3,'morrisons':3,'sainsburys':2.5,'tesco':2.5}
    for (shop_num = 0; shop_num < shop_data.length; shop_num++){
        shop=shop_data[shop_num][0]['shop']
        newist_price=shop_data[shop_num][shop_data[shop_num].length-1]['price']
        diffrence = newist_price-default_prices[shop]

        if (diffrence > 0){
            symbol = ' ▲ ' + "(" + diffrence + ")"
            document.getElementById(shop).style.backgroundColor = "#BF0603";
        }
        else if (diffrence < 0){
           symbol = ' ▼ ' + "(" + diffrence + ")"
           document.getElementById(shop).style.backgroundColor = "#5ec100";

        }
        else {
            symbol=' ━ ' + "(" + diffrence + ")"
        }

        var name_node = document.createElement("p");
        var name_textnode = document.createTextNode(shop);
        name_node.appendChild(name_textnode);

        var price_node = document.createElement("p");
        var price_textnode = document.createTextNode(newist_price+symbol);
        price_node.appendChild(price_textnode);

        document.getElementById(shop).appendChild(name_node);
        document.getElementById(shop).appendChild(price_node);

    }

}