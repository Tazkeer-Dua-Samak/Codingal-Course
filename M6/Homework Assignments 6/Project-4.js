let totalIncome = 0;
let totalExpense = 0;

document.getElementById('trackerForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const income = parseFloat(document.getElementById('income').value);
    const expense = parseFloat(document.getElementById('expense').value);
    totalIncome += income;
    totalExpense += expense;
    document.getElementById('totalIncome').innerText = totalIncome;
    document.getElementById('totalExpense').innerText = totalExpense;
    document.getElementById('balance').innerText = totalIncome - totalExpense;
    this.reset();
});