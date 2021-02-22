document.addEventListener('DOMContentLoaded', () => {
  fetch("/prices/" + ticker)
    .then((response) => response.json())
    .then((result) => {
      console.log(result['prices']);
      prices = result['prices'];
      document.querySelector('#current_price').textContent = prices[29].toFixed(2);
      document.querySelector('#predicted_price').textContent = prices[36].toFixed(2);
      var xvals = [];

      for (var i = -29; i <= 7; i++) {
        xvals.push(i);
      }
      var ctx = document.getElementById('myChart');
      data = []
      for (let i = 0; i < 37; i++) {
        data.push({x:xvals[i],y:prices[i].toFixed(2)});
      }
      console.log(data)
      var x = new Chart(ctx, {
         type: 'scatter',
         data: {
            datasets: [{
               pointBackgroundColor: "#2670FF",
               label: "Stocks over Time",
               data: data,
            }]
         },
         options: {
            responsive: true
         }
      });
});
});
