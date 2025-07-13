#--------------------------------------------Task:-------------------------------------------------#
#Transform Acad to astro hours.
academical_hours = 64
acad_hour_minutes = 40
session_size = 4
break_minutes = 20
astro_hour_minutes = 60

sessions = academical_hours // session_size

total_minutes = academical_hours * acad_hour_minutes + sessions * break_minutes


total_astro_hours = total_minutes / astro_hour_minutes

print(f"Total duration in astronomical hours: {total_astro_hours:.2f}")
#--------------------------------------------------------------------------------------------------#