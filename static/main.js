document.addEventListener('DOMContentLoaded', async () => {
  const socket = io();
  const form = document.getElementById('reportForm');
  const feed = document.getElementById('feed');

  // Submit form
  form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const data = {
      location: form.location.value,
      type: form.type.value,
      message: form.message.value,
    };

    await fetch('/report', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data),
    });

    form.reset();
  });

  // Load existing reports once
  const res = await fetch('/reports');
  const reports = await res.json();
  reports.forEach(report => {
    const item = document.createElement('li');
    item.textContent = `${report.type} at ${report.location}: ${report.message}`;
    feed.appendChild(item);
  });

  // Listen for new reports
  socket.on('new_report', (report) => {
    const item = document.createElement('li');
    item.textContent = `${report.type} at ${report.location}: ${report.message}`;
    feed.prepend(item);
  });
});

document.addEventListener('DOMContentLoaded', () => {
  const locationInput = document.querySelector('input[name="location"]');
  const autocomplete = new google.maps.places.Autocomplete(locationInput);
});


