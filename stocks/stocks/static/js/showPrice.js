document.addEventListener('DOMContentLoaded', () => {
fetch("/prices/"+ticker)
.then((response) => response.json())
.then((result) => {
  prices = result['prices']
  document.querySelector('#current_price').textContent=prices[29].toFixed(2)
  document.querySelector('#predicted_price').textContent = prices[36].toFixed(2)
  var trace1 = {
    x: [1, 2, 3, 4],
    y: prices,
    mode: 'markers',
    type: 'scatter'
  };

  var data = [trace1];

  var layout = {
    title:'Past and Predicted Price',

     xaxis: {
      title: 'Trading Day',
    },
    yaxis: {
      title: 'Price',
    },

    xaxis: {
    range: [-30, 7]
  },
  };

  Plotly.newPlot('graph', data);
});
});
