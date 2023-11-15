const ctx = document.getElementById('myChart');
let goal = 7;
let current = 1;
new Chart(ctx, {
  type: 'doughnut',
  data: {
    labels: ['Workout', 'Remaining'],
    datasets: [{
      label: 'Current goal',
      data: [goal, 0],
      backgroundColor: [
        'rgb(144, 237, 144)',
        'rgb(144, 237, 144)'
      ]
    },
    {
      label: 'Current progress',
      data: [current, goal - current],
      backgroundColor: [
        'rgb(52, 207, 235)',
        'rgb(128, 128, 128)'
      ]
    }]
  },
  options: {
    responsive: true,
    plugins: {
      legend: {
        display: false,
      },
      title: {
        display: true,
        text: 'Workout Progression'
      }
    }
  }
});
