document.addEventListener('DOMContentLoaded', () => {
fetch(`/prices/{ticker}`)
.then((response) => response.json())
.then((result) => {
  console.log(result)
  var trace1 = {
    x: [-29, -28, -27, -26, -25, -24, -23, -22, -21, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11,
    -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7],
    y: result['prices'],
    type: 'scatter',
    mode: 'lines',
    line: {
        color: 'rgb(0,0,0)',
        width: 5
      }
  };
  console.log(trace1)
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

  Plotly.plot('graph', data,layout);
});
});
