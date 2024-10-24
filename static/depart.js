document.addEventListener('DOMContentLoaded', function() {
    var ctxLine = document.getElementById('lineChart').getContext('2d');
    var lineChart = new Chart(ctxLine, {
        type: 'line',
        data: {
            labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug'],
            datasets: [{
                label: 'Progress in years',
                data: [2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010],
                borderColor: '#8d6bc7',
                backgroundColor: 'rgba(76, 161, 175, 0.2)',
                fill: true,
                tension: 0.1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false
        }
    });

    var ctxRadial1 = document.getElementById('radialChart1').getContext('2d');
    var radialChart1 = new Chart(ctxRadial1, {
        type: 'doughnut',
        data: {
            datasets: [{
                // lable:'IT',     // to add the lable content in the radial chart graph 
                data: [65, 35],
                backgroundColor: ['#8d6bc7', '#d667b7']
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            cutout: '70%'
        }
    });

    var ctxRadial2 = document.getElementById('radialChart2').getContext('2d');
    var radialChart2 = new Chart(ctxRadial2, {
        type: 'doughnut',
        data: {
            datasets: [{
                data: [55, 45],
                backgroundColor: ['#8d6bc7', '#d667b7']
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            cutout: '70%'
        }
    });

    var ctxRadial3 = document.getElementById('radialChart3').getContext('2d');
    var radialChart3 = new Chart(ctxRadial3, {
        type: 'doughnut',
        data: {
            datasets: [{
                data: [27, 73],
                backgroundColor: ['#8d6bc7', '#d667b7']
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            cutout: '70%'
        }
    
    });
});
 // Assuming you have a logout function
 function logout() {
    // Perform logout actions here, such as clearing session, redirecting, etc.
    alert("You have been logged out."); // Example alert
    // Example: Redirect to login page
    window.location.href = "login.html";
}

// Add event listener to logout button
var logoutButton = document.getElementById("logoutButton");
logoutButton.addEventListener("click", logout);
