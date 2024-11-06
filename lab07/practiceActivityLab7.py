# The purpose of this practice activity for Lab 7 is to design a table for my class schedule for Fall Semester 2024 using html & CSS.
<!DOCTYPE html5>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Daveed A. Sumpter's CCBC 2024 Fall Semester Class Schedule and Program of Study Form</title>
    <link rel="stylesheet" href="style.css">
    <style>
    .content-table{
        border-collapse: collapse;  # Reduces the amount of space.
        margin: 25px 0;
        font-size: 0.9em;
        min-width: 400px;
        border-radius: 5px 5px 0 0;  # Creates rounded edges.
        overflow: hidden;            # Helps to display border-radius.
        box-shadow: 0 0 20px rgba(0,0,0,0.15);
        }
    .content-table thead tr{
        background-color:
        color:
        text-align: left;
        font-weight: bold;           # Heading columns are bold.
    }
    .content-table th,
    .content-table td {
        padding: 12px 15px;
    }
    .content-table tbody tr{         # Targets table rows in table body.
        border-bottom: 1px solid color;
    }
    .content-table tbody tr: nth-of-type(even){      # Targets table rows in table body.
        background-color: grey;
    }
    .content-table tbdoy tr: last-of-type{           # Targets last table row in table body.
        border-bottom: 2px solid color;
    }
    .content-table tbdoy tr.active-row{
        font-weight: bold;
        color: red;
    }

    </style>
</head>
<body>
  <nav>
    <a href="contact.html">Link to Contact Page</a>
  </nav>
  <h1>My 2024 Fall Semester Class Schedule</h1>
  <table>
    <thead>
        <tr>
           <th scope="col">Tier</th>
           <th scope="col">Class Number 1</th>
           <th scope="col">Class Number 2</th>
        </tr>
    </thead>
    <tbody>
        <tr id="s_Tier">
            <td>S</td>
            <td><img id="programming" src=".jpg" alt="This is a photo of a computer programmer"></td>
            <td><img id="web standards" src=".jpg" alt="This is a photo of a web developer"></td>
        </tr>
        <tr id="a_Tier">
            <td>A</td>
            
   <form>
      <div>
         <label for="fname">first name:</label>
            <input type="text" id="fname" name="fname" placeholder="Abraham">
      </div>
      <div>
        <label for="lname">last name:</label>
            <input type="text" id="lname" name="lname" placeholder="Lincoln">
      </div>
      <div>
            <input type="reset">
      </div>
      <div>
            <input type="submit">
      </div>
      <div>
            <label for="pass">password:</label>
            <input type="password" id="pass" name="pass" maxlength="12" required>
      </div>
      <div>
            <label for="email">email:</label>
            <input type="email" id="email" name="email" placeholder="SPants@gmail.com">
      </div>
      <div>
            <label for="phone">phone #:</label>
            <input type="tel" id="phone" name="phone" placeholder="(123)-456-7890">
      </div>
      <div>
            <label for="bdate">birthdate:</label>
            <input type="date" id="bdate" name="bdate">
      </div>
      <div>
            <label for="title">title:</label>
            <label for="Mr.">Mr.</label>
            <input type="radio" id="Mr." name="title" value="Mr.">
      </div>
      <div>
            <label for="title">title:</label>
            <label for="Ms.">Ms.</label>
            <input type="radio" id="Ms." name="title" value="Ms.">
      </div>
      <div>
            <label for="title">title:</label>
            <label for="Mrs.">Mrs.</label>
            <input type="radio" id="Mrs." name="title" value="Mrs.">
      </div>
      <div>
            <label for="program type">program type:</label>
            <label for="Associate of Arts">Associate of Arts</label>
            <input type="checkbox" id="Associate of Arts" name="program type" value="Associate of Arts">

    <nav>




