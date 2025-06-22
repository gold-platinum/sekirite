# Sekirite

## Inspiration
Haiti faces an extreme case of gang violence. Just last year, over 5000 people died from the chaos. One reason for these deaths is that people aren't informed of suspicious activity beforehand. Haiti doesn't have access to apps like Citizen.

## What it does
Sekirite (Safety in Haitian Creole) is a real-time incident reporting app to keep communities safe from gang violence. You can file reports with the location, type of situation, and a short message. These reports will show up in a live feed, which will warn others, promoting their safety.

## How we built it
This program is built using Flask for the backend and Socket.IO for real-time communication. It integrates Firebase Realtime Database to store and retrieve incident reports. The frontend is built with vanilla JavaScript and HTML/CSS, enabling users to submit reports and view a live feed of incidents.

## Challenges we ran into
One of the key challenges we faced was integrating Firebase in Python, as different libraries offer different levels of support—some lacking essential methods like .child(), which required restructuring how we accessed and stored data. On the frontend, we ran into issues with duplicate script execution, which caused reports to appear multiple times due to multiple event listeners being attached. Managing real-time updates through Socket.IO also required careful coordination to avoid redundant updates and ensure a smooth user experience. 

## Accomplishments that we're proud of
One thing we are especially proud of was the implementation of real-time functionality works—new reports appear instantly across all clients without needing a page refresh, thanks to the integration of Flask with Socket.IO. 

## What we learned
One key thing we learned is the importance of understanding how third-party libraries differ in functionality, especially when working with Firebase in Python. Not all libraries support the same methods, and assuming they do can lead to unexpected bugs. This taught us to read documentation closely, test incrementally, and adapt our architecture based on the tools' actual capabilities rather than their assumed ones.

## What's next for Sekirite
We are planning on adding a map view. On it, there will be pins pertaining to incident. We are also planning on adding secured encryption and the ability to call authorities or other NGO's. We also plan to port this app to mobiles.
