document.addEventListener('DOMContentLoaded', () => {
  fetch("/prices/" + ticker)
    .then((response) => response.json())
    .then((result) => {
      console.log(result['prices'])
      var xvals = [];

      for (var i = 1; i <= 37; i++) {
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
          range: [-30, 7]
        },
      };

      Plotly.newPlot('graph', data);
    });
});
