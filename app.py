
import tkinter as tk
from src.helpers import set_background, clear_widgets


root = tk.Tk()
root.title("GymGirls")
root.geometry("430x530")

#reference:https://github.com/shaq31415926/python_tech_basics/blob/main/tech_basics_two/13Lecture/app.py
#returns to home page "hi gymgirl" once you have set up your profile
def new_page_setup(root):

    # this clear all the widgets that have been created
    clear_widgets(root)

    # add a home page button - this will go back to our home page
    homepage = tk.Button(root,
                         text="🏠",
                         command=lambda: gymgirl_homepage(root)
                         )
    homepage.place(relx=0.4, rely=0.92)

# creates exit button
def exit_button(root):
    exit_button = tk.Button(text="X",
                            font=("Comic Sans MS", 14, "bold"),
                            fg= "red",
                            bg="grey",
                            command=root.destroy
                            )
    exit_button.grid(column=0, row=4, padx=10, pady=10)
    exit_button.place(relx=0.85,
                      rely=0.925)
def login_frame(root):


    # setting background to black

    set_background(root, "images/homepage_background.png")

    exit_button(root)

    # Widgets for the first frame
    # creates username and password label
    # sets font
    # creates entry boxes for username and password

    label_username = tk.Label(root, text="Username:", fg="VioletRed3", font=("Helvetica", 22), bg="white")
    label_username.place(relx=0.1, rely=0.2)

    entry_username = tk.Entry(root)
    entry_username.place(relx=0.4, rely=0.2)

    label_password = tk.Label(root, text="Password:", fg="VioletRed3", font=("Helvetica", 22), bg="white")
    label_password.place(relx=0.1, rely=0.4)

    # shows * instead of letters for password
    entry_password = tk.Entry(root, show="*")
    entry_password.place(relx=0.4, rely=0.4)

    # Creates a button widget to join and a command to execute when clicked
    join_button = tk.Button(root, text="Join GymGirls", font=("Helvetica", 22), command=lambda: welcome_frame(root))
    join_button.place(relx=0.3, rely=0.6)



# creates main frame
def welcome_frame(root):
    clear_widgets(root)

    exit_button(root)

    set_background(root, "images/homepage_background.png")


    exit_button(root)
    # Widgets for the main frame
    label_welcome = tk.Label(root, text="Welcome to GymGirls!", font=("Helvetica", 22))
    label_welcome.place(relx=0.15, rely=0.3)

    profile_button = tk.Button(root, text="Create Your Profile",font=("Helvetica", 22), command=lambda: create_profile_frame(root))
    profile_button.place(relx=0.2, rely=0.5)

    Back_to_login_Button = tk.Button(root, text="⬅️", command=lambda: login_frame(root))
    Back_to_login_Button.place(relx=0.1, rely=0.92)

# defines what happens when create profile is clicked
def create_profile_frame(root):

    clear_widgets(root)

    root.configure(background="#FFE1FF")

    exit_button(root)
    # Widgets for the profile frame
    label_profile = tk.Label(root, text="Create Your Profile", font=("Helvetica", 20))
    label_profile.place(relx=0.2,rely=0)

    # Add profile labels and input fields
    label_name = tk.Label(root, text="Name:", font=("Helvetica", 16))
    label_name.place(relx=0,rely=0.1)

    entry_name = tk.Entry(root)
    entry_name.place(relx=0.4,rely=0.1)

    label_age = tk.Label(root, text="Age:",  font=("Helvetica", 16))
    label_age.place(relx=0,rely=0.2)

    entry_age = tk.Entry(root)
    entry_age.place(relx=0.4,rely=0.2)

    label_membership = tk.Label(root, text="Gym Membership:",font=("Helvetica", 16) )
    label_membership.place(relx=0,rely=0.3)

    #  dropdown menu for membership status
    # reference https://www.geeksforgeeks.org/dropdown-menus-tkinter/
    membership_options = ["Yes", "No"]
    var_membership = tk.StringVar(root)
    var_membership.set(membership_options[0])  # Default value
    dropdown_membership = tk.OptionMenu(root, var_membership, *membership_options)
    dropdown_membership.place(relx=0.4,rely=0.3)

    label_yes_no = tk.Label(root, text="if yes which one:",font=("Helvetica", 16))
    label_yes_no.place(relx=0,rely=0.4)

    entry_yes_no = tk.Entry(root)
    entry_yes_no.place(relx=0.4,rely=0.4)

    label_goals = tk.Label(root, text="Fitness Goals:", font=("Helvetica", 16))
    label_goals.place(relx=0,rely=0.5)

    entry_goals = tk.Entry(root)
    entry_goals.place(relx=0.4,rely=0.5)

    # Adds a button to save the profile
    save_button = tk.Button(root, text="Save Profile", font=("Helvetica", 20), command=lambda: saved_profile_frame(root))
    save_button.place(relx=0.3,rely=0.7)

    Back_to_welcome_Button = tk.Button(root, text="⬅️", command=lambda: welcome_frame(root))
    Back_to_welcome_Button.place(relx=0.1, rely=0.92)

# defines what happens when save profile is clicked
def saved_profile_frame(root):

    clear_widgets(root)

    exit_button(root)

    root.configure(background="#FFE1FF")

    # widgets for profile saved frame
    label_saved_profile = tk.Label(root, text="Profile Saved!", font=("Helvetica", 22))
    label_saved_profile.place(relx=0.3,rely=0.3)

    button_getstarted = tk.Button(root, text="Get started", font=("Helvetica", 26), command=lambda: gymgirl_homepage(root))
    button_getstarted.place(relx=0.27,rely=0.5)

    Back_to_create_profile_Button = tk.Button(root, text="⬅️", command=lambda: create_profile_frame(root))
    Back_to_create_profile_Button.place(relx=0.1, rely=0.92)

# defines what happens when get started is clicked
def gymgirl_homepage(root):

    clear_widgets(root)

    set_background(root, "images/homepage_background.png")
    exit_button(root)

    root.configure(background="#FFE1FF")

    label_welcome = tk.Label(root, text="Hi GymGirl!", font=("Helvetica", 22))
    label_welcome.place(relx=0.3,rely=0.05)

    # Adds buttons for different actions
    share_training_button = tk.Button(root, text="About GymGirls", font=("georgia",24), command=lambda: about_us(root))
    share_training_button.place(relx=0.2,rely=0.2)

    connect_button = tk.Button(root, text="Connect with Gym Girls", font=("georgia",24),command=lambda: connect_with_gym_girls(root))
    connect_button.place(relx=0.17,rely=0.35)

    find_gyms_button = tk.Button(root, text="Share Your Training",font=("georgia",24), command=lambda: share_training(root))
    find_gyms_button.place(relx=0.2,rely=0.5)

    share_experiences_button = tk.Button(root, text="Share Experiences", font=("georgia",24), command=lambda: share_experiences(root))
    share_experiences_button.place(relx=0.2,rely=0.65)

    profile_button= tk.Button(root, text="👤 Your Profile", command=lambda:user_profile(root))
    profile_button.place(relx=0.7,rely=0.05)

    Back_to_save_profile_Button = tk.Button(root, text="⬅️", command=lambda: create_profile_frame(root))
    Back_to_save_profile_Button.place(relx=0.1, rely=0.92)

def user_profile(root):
    new_page_setup(root)

def about_us(root):
    new_page_setup(root)


def connect_with_gym_girls(root):

    set_background(root, "images/gyms_near_me.jpeg")


    pin1_button = tk.Button(root, text="📍", command=lambda: Gym_A(root))
    pin1_button.place(relx=0.5,
                      rely=0.6,
                      )

    pin2_button = tk.Button(root, text="📍", command=lambda: Gym_B(root))
    pin2_button.place(relx=0.2,
                      rely=0.3,
                      )

    pin3_button = tk.Button(root, text="📍", command=lambda: Gym_C(root))
    pin3_button.place(relx=0.6,
                      rely=0.4,
                      )

    home_button = tk.Button(root, text="🏠", command=lambda: gymgirl_homepage(root))
    home_button.place(relx=0.4, rely=0.92)


def Gym_A(root):
    new_page_setup(root)

    label_Gym_A = tk.Label(root, text="Fitness St.Georg", font=("Helvetica", 16))
    label_Gym_A.place(relx=0.3,rely=0)

    Lisa_B_Button = tk.Button(root, text="Get to know Lisa B.", command=lambda:Lisa_B_profile(root))
    Lisa_B_Button.place(relx=0.1, rely=0.2)

    Sarah_M_Button = tk.Button(root, text="Get to know Sarah M.", command=lambda:Sarah_M_profile(root))
    Sarah_M_Button.place(relx=0.1, rely=0.3)

    Back_to_Map_Button = tk.Button(root, text= "Back to Map", command=lambda:connect_with_gym_girls(root))
    Back_to_Map_Button.place(relx=0.7, rely=0.92)


def Lisa_B_profile(root):
    new_page_setup(root)

    set_background(root, "images/Lisa_B.png")

    Back_to_Map_Button = tk.Button(root, text="Back to Map", command=lambda: connect_with_gym_girls(root))
    Back_to_Map_Button.place(relx=0.7, rely=0.92)

    Back_to_Gym_A_Button = tk.Button(root, text="⬅️", command=lambda:Gym_A(root))
    Back_to_Gym_A_Button.place(relx=0.1,rely=0.92)
def Sarah_M_profile(root):
    new_page_setup(root)

    set_background(root, "images/Sarah_M.png")

    Back_to_Map_Button = tk.Button(root, text="Back to Map", command=lambda: connect_with_gym_girls(root))
    Back_to_Map_Button.place(relx=0.7, rely=0.92)

    Back_to_Gym_A_Button = tk.Button(root, text="⬅️", command=lambda: Gym_A(root))
    Back_to_Gym_A_Button.place(relx=0.1, rely=0.92)
def Gym_B(root):
    new_page_setup(root)

    label_Gym_B = tk.Label(root, text="Fitness Eimsbüttel", font=("Helvetica", 16))
    label_Gym_B.place(relx=0.3, rely=0)

    Lily_S_Button = tk.Button(root, text="Get to know Lily S.", command=lambda: Lily_S_profile(root))
    Lily_S_Button.place(relx=0.1, rely=0.2)

    Back_to_Map_Button = tk.Button(root, text="Back to Map", command=lambda: connect_with_gym_girls(root))
    Back_to_Map_Button.place(relx=0.7, rely=0.92)

    Back_to_Gym_B_Button = tk.Button(root, text="⬅️", command=lambda: Gym_B(root))
    Back_to_Gym_B_Button.place(relx=0.1, rely=0.92)

def Lily_S_profile(root):
    new_page_setup(root)

    set_background(root, "images/Lily_S.png")

    Back_to_Map_Button = tk.Button(root, text="Back to Map", command=lambda: connect_with_gym_girls(root))
    Back_to_Map_Button.place(relx=0.7, rely=0.92)
def Gym_C(root):
    new_page_setup(root)

    label_Gym_C = tk.Label(root, text="Fitness Barmbek", font=("Helvetica", 16))
    label_Gym_C.place(relx=0.3, rely=0)

    label_no_users = tk.Label(root, text="No GymGirls yet ☹️", font=("Helvetica", 20))
    label_no_users.place(relx=0.2, rely=0.1)

    label_tell_your_friends = tk.Label(root, text="Tell Your Friends About Us!!!!️", font=("Helvetica", 20))
    label_tell_your_friends.place(relx=0.15, rely=0.2)


    Back_to_Map_Button = tk.Button(root, text="Back to Map", command=lambda: connect_with_gym_girls(root))
    Back_to_Map_Button.place(relx=0.7, rely=0.92)

def share_training(root):
    new_page_setup(root)

def share_experiences(root):
    new_page_setup(root)


login_frame(root)

root.mainloop()
