       
        // Function to check Whether both passwords
        // is same or not.
        function checkPassword(form) {
            password1 = form.password.value;
            password2 = form.passconfirm.value;

            // If password not entered
            if (password == '')
                alert ("Please enter Password");
                  
            // If confirm password not entered
            else if (passconfirm == '')
                alert ("Please enter confirm password");
                  
            // If Not same return False.    
            else if (password != passconfirm) {
                alert ("\nPassword did not match: Please try again...")
                return false;
            }

            // If same return True.
            else{
                alert("Password Match: Welcome to Medic booking app!")
                return true;
            }
        }