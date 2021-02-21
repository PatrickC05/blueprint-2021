document.addEventListener('DOMContentLoaded', () => {
  fetch("/prices/" + ticker)
    .then((response) => response.json())
    .then((result) => {
      console.log(result['prices'])
      var xvals = [];

      for (var i = -29; i <= 7; i++) {
        xvals.push(i);
      }
      var trace1 = {
        x: xvals,
        y: result['prices'],
        mode: 'markers',
        type: 'scatter'
      };

      var data = [trace1];

      var layout = {
        title: 'Past and Predicted Price',

        xaxis: {
          title: 'Trading Day',
        },
        yaxis: {
          title: 'Price',
        },

        xaxis: {
          range: [-29, 7]
        },
      };

      Plotly.newPlot('graph', data, layout);
    });
});
