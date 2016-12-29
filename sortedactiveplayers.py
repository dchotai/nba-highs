"""
From stats.nba.com Player Index, players are sorted by team
[PlayerID, "LastName, FirstName", Active(1=Yes, 0=No), FirstSeasonActive, LastSeasonActive, TeamID, ...]
"""
players = {
    1610612737: [
        [203145, 'Bazemore, Kent', 1, 2012, 2016, 1610612737, 'Y'],
        [1627761, "Bembry, DeAndre'", 1, 2016, 2016, 1610612737, 'Y'],
        [1627098, 'Delaney, Malcolm', 1, 2016, 2016, 1610612737, 'Y'],
        [203501, 'Hardaway Jr., Tim', 1, 2013, 2016, 1610612737, 'Y'],
        [2730, 'Howard, Dwight', 1, 2004, 2016, 1610612737, 'Y'],
        [2743, 'Humphries, Kris', 1, 2004, 2016, 1610612737, 'Y'],
        [203527, 'Kelly, Ryan', 1, 2013, 2016, 1610612737, 'Y'],
        [2594, 'Korver, Kyle', 1, 2003, 2016, 1610612737, 'Y'],
        [200794, 'Millsap, Paul', 1, 2006, 2016, 1610612737, 'Y'],
        [203488, 'Muscala, Mike', 1, 2013, 2016, 1610612737, 'Y'],
        [1627752, 'Prince, Taurean', 1, 2016, 2016, 1610612737, 'Y'],
        [203471, 'Schroder, Dennis', 1, 2013, 2016, 1610612737, 'Y'],
        [203118, 'Scott, Mike', 1, 2012, 2016, 1610612737, 'Y'],
        [200757, 'Sefolosha, Thabo', 1, 2006, 2016, 1610612737, 'Y'],
        [201168, 'Splitter, Tiago', 1, 2010, 2016, 1610612737, 'Y']
    ],
    1610612738: [
        [202340, 'Bradley, Avery', 1, 2010, 2016, 1610612738, 'Y'],
        [1627759, 'Brown, Jaylen', 1, 2016, 2016, 1610612738, 'Y'],
        [203109, 'Crowder, Jae', 1, 2012, 2016, 1610612738, 'Y'],
        [101123, 'Green, Gerald', 1, 2005, 2016, 1610612738, 'Y'],
        [201143, 'Horford, Al', 1, 2007, 2016, 1610612738, 'Y'],
        [1627743, 'Jackson, Demetrius', 1, 2016, 2016, 1610612738, 'Y'],
        [201973, 'Jerebko, Jonas', 1, 2009, 2016, 1610612738, 'Y'],
        [101161, 'Johnson, Amir', 1, 2005, 2016, 1610612738, 'Y'],
        [1626175, 'Mickey, Jordan', 1, 2015, 2016, 1610612738, 'Y'],
        [203482, 'Olynyk, Kelly', 1, 2013, 2016, 1610612738, 'Y'],
        [1626179, 'Rozier, Terry', 1, 2015, 2016, 1610612738, 'Y'],
        [203935, 'Smart, Marcus', 1, 2014, 2016, 1610612738, 'Y'],
        [202738, 'Thomas, Isaiah', 1, 2011, 2016, 1610612738, 'Y'],
        [203923, 'Young, James', 1, 2014, 2016, 1610612738, 'Y'],
        [203092, 'Zeller, Tyler', 1, 2012, 2016, 1610612738, 'Y']
    ],
    1610612739: [
        [2365, 'Andersen, Chris', 1, 2001, 2016, 1610612739, 'Y'],
        [2399, 'Dunleavy, Mike', 1, 2002, 2016, 1610612739, 'Y'],
        [1627770, 'Felder, Kay', 1, 2016, 2016, 1610612739, 'Y'],
        [101112, 'Frye, Channing', 1, 2005, 2016, 1610612739, 'Y'],
        [202681, 'Irving, Kyrie', 1, 2011, 2016, 1610612739, 'Y'],
        [2544, 'James, LeBron', 1, 2003, 2016, 1610612739, 'Y'],
        [2210, 'Jefferson, Richard', 1, 2001, 2016, 1610612739, 'Y'],
        [2592, 'Jones, James', 1, 2003, 2016, 1610612739, 'Y'],
        [202732, 'Liggins, DeAndre', 1, 2011, 2016, 1610612739, 'Y'],
        [201567, 'Love, Kevin', 1, 2008, 2016, 1610612739, 'Y'],
        [203895, 'McRae, Jordan', 1, 2015, 2016, 1610612739, 'Y'],
        [202697, 'Shumpert, Iman', 1, 2011, 2016, 1610612739, 'Y'],
        [2747, 'Smith, JR', 1, 2004, 2016, 1610612739, 'Y'],
        [202684, 'Thompson, Tristan', 1, 2011, 2016, 1610612739, 'Y'],
        [2590, 'Williams, Mo', 1, 2003, 2016, 1610612739, 'Y']
    ],
    1610612740: [
        [201582, 'Ajinca, Alexis', 1, 2008, 2016, 1610612740, 'Y'],
        [201600, 'Asik, Omer', 1, 2010, 2016, 1610612740, 'Y'],
        [201967, 'Cunningham, Dante', 1, 2009, 2016, 1610612740, 'Y'],
        [203076, 'Davis, Anthony', 1, 2012, 2016, 1610612740, 'Y'],
        [1627767, 'Diallo, Cheick', 1, 2016, 2016, 1610612740, 'Y'],
        [201936, 'Evans, Tyreke', 1, 2009, 2016, 1610612740, 'Y'],
        [204025, 'Frazier, Tim', 1, 2014, 2016, 1610612740, 'Y'],
        [204038, 'Galloway, Langston', 1, 2014, 2016, 1610612740, 'Y'],
        [1627741, 'Hield, Buddy', 1, 2016, 2016, 1610612740, 'Y'],
        [203524, 'Hill, Solomon', 1, 2013, 2016, 1610612740, 'Y'],
        [201950, 'Holiday, Jrue', 1, 2009, 2016, 1610612740, 'Y'],
        [203093, 'Jones, Terrence', 1, 2012, 2016, 1610612740, 'Y'],
        [202734, "Moore, E'Twaun", 1, 2011, 2016, 1610612740, 'Y'],
        [202347, 'Pondexter, Quincy', 1, 2010, 2016, 1610612740, 'Y'],
        [202130, 'Williams, Reggie', 1, 2009, 2016, 1610612740, 'Y']
    ],
    1610612741: [
        [202710, 'Butler, Jimmy', 1, 2011, 2016, 1610612741, 'Y'],
        [203477, 'Canaan, Isaiah', 1, 2013, 2016, 1610612741, 'Y'],
        [203487, 'Carter-Williams, Michael', 1, 2013, 2016, 1610612741, 'Y'],
        [1626245, 'Felicio, Cristiano', 1, 2015, 2016, 1610612741, 'Y'],
        [201959, 'Gibson, Taj', 1, 2009, 2016, 1610612741, 'Y'],
        [1626170, 'Grant, Jerian', 1, 2015, 2016, 1610612741, 'Y'],
        [1626154, 'Hunter, RJ', 1, 2015, 2016, 1610612741, 'Y'],
        [201577, 'Lopez, Robin', 1, 2008, 2016, 1610612741, 'Y'],
        [203926, 'McDermott, Doug', 1, 2014, 2016, 1610612741, 'Y'],
        [202703, 'Mirotic, Nikola', 1, 2014, 2016, 1610612741, 'Y'],
        [1626171, 'Portis, Bobby', 1, 2015, 2016, 1610612741, 'Y'],
        [200765, 'Rondo, Rajon', 1, 2006, 2016, 1610612741, 'Y'],
        [1627756, 'Valentine, Denzel', 1, 2016, 2016, 1610612741, 'Y'],
        [2548, 'Wade, Dwyane', 1, 2003, 2016, 1610612741, 'Y'],
        [1627835, 'Zipser, Paul', 1, 2016, 2016, 1610612741, 'Y']
    ],
    1610612742: [
        [1626147, 'Anderson, Justin', 1, 2015, 2016, 1610612742, 'Y'],
        [200826, 'Barea, J.J.', 1, 2006, 2016, 1610612742, 'Y'],
        [203084, 'Barnes, Harrison', 1, 2012, 2016, 1610612742, 'Y'],
        [101106, 'Bogut, Andrew', 1, 2005, 2016, 1610612742, 'Y'],
        [1627852, 'Brussino, Nicolas', 1, 2016, 2016, 1610612742, 'Y'],
        [203552, 'Curry, Seth', 1, 2013, 2016, 1610612742, 'Y'],
        [1627827, 'Finney-Smith, Dorian', 1, 2016, 2016, 1610612742, 'Y'],
        [1626780, 'Gibson, Jonathan', 1, 2016, 2016, 1610612742, 'Y'],
        [1627773, 'Hammons, AJ', 1, 2016, 2016, 1610612742, 'Y'],
        [2734, 'Harris, Devin', 1, 2004, 2016, 1610612742, 'Y'],
        [202083, 'Matthews, Wesley', 1, 2009, 2016, 1610612742, 'Y'],
        [1626257, 'Mejri, Salah', 1, 2015, 2016, 1610612742, 'Y'],
        [1717, 'Nowitzki, Dirk', 1, 1998, 2016, 1610612742, 'Y'],
        [203939, 'Powell, Dwight', 1, 2014, 2016, 1610612742, 'Y'],
        [101114, 'Williams, Deron', 1, 2005, 2016, 1610612742, 'Y']
    ],
    1610612743: [
        [201589, 'Arthur, Darrell', 1, 2008, 2016, 1610612743, 'Y'],
        [203115, 'Barton, Will', 1, 2012, 2016, 1610612743, 'Y'],
        [1627736, 'Beasley, Malik', 1, 2016, 2016, 1610612743, 'Y'],
        [201163, 'Chandler, Wilson', 1, 2007, 2016, 1610612743, 'Y'],
        [202702, 'Faried, Kenneth', 1, 2011, 2016, 1610612743, 'Y'],
        [201568, 'Gallinari, Danilo', 1, 2008, 2016, 1610612743, 'Y'],
        [202087, 'Gee, Alonzo', 1, 2009, 2016, 1610612743, 'Y'],
        [203914, 'Harris, Gary', 1, 2014, 2016, 1610612743, 'Y'],
        [1627823, 'Hernangomez, Juan', 1, 2016, 2016, 1610612743, 'Y'],
        [203999, 'Jokic, Nikola', 1, 2015, 2016, 1610612743, 'Y'],
        [2034, 'Miller, Mike', 1, 2000, 2016, 1610612743, 'Y'],
        [1626144, 'Mudiay, Emmanuel', 1, 2015, 2016, 1610612743, 'Y'],
        [1627750, 'Murray, Jamal', 1, 2016, 2016, 1610612743, 'Y'],
        [2749, 'Nelson, Jameer', 1, 2004, 2016, 1610612743, 'Y'],
        [203994, 'Nurkic, Jusuf', 1, 2014, 2016, 1610612743, 'Y']
    ],
    1610612744: [
        [203546, 'Clark, Ian', 1, 2013, 2016, 1610612744, 'Y'],
        [201939, 'Curry, Stephen', 1, 2009, 2016, 1610612744, 'Y'],
        [201142, 'Durant, Kevin', 1, 2007, 2016, 1610612744, 'Y'],
        [203110, 'Green, Draymond', 1, 2012, 2016, 1610612744, 'Y'],
        [2738, 'Iguodala, Andre', 1, 2004, 2016, 1610612744, 'Y'],
        [1627745, 'Jones, Damian', 1, 2016, 2016, 1610612744, 'Y'],
        [2733, 'Livingston, Shaun', 1, 2004, 2016, 1610612744, 'Y'],
        [1626172, 'Looney, Kevon', 1, 2015, 2016, 1610612744, 'Y'],
        [203949, 'McAdoo, James Michael', 1, 2014, 2016, 1610612744, 'Y'],
        [1627775, 'McCaw, Patrick', 1, 2016, 2016, 1610612744, 'Y'],
        [201580, 'McGee, JaVale', 1, 2008, 2016, 1610612744, 'Y'],
        [2585, 'Pachulia, Zaza', 1, 2003, 2016, 1610612744, 'Y'],
        [202691, 'Thompson, Klay', 1, 2011, 2016, 1610612744, 'Y'],
        [2760, 'Varejao, Anderson', 1, 2004, 2016, 1610612744, 'Y'],
        [2561, 'West, David', 1, 2003, 2016, 1610612744, 'Y']
    ],
    1610612745: [
        [201583, 'Anderson, Ryan', 1, 2008, 2016, 1610612745, 'Y'],
        [2772, 'Ariza, Trevor', 1, 2004, 2016, 1610612745, 'Y'],
        [201976, 'Beverley, Patrick', 1, 2012, 2016, 1610612745, 'Y'],
        [201147, 'Brewer, Corey', 1, 2007, 2016, 1610612745, 'Y'],
        [201628, 'Brown, Bobby', 1, 2008, 2016, 1610612745, 'Y'],
        [203991, 'Capela, Clint', 1, 2014, 2016, 1610612745, 'Y'],
        [1626155, 'Dekker, Sam', 1, 2015, 2016, 1610612745, 'Y'],
        [203898, 'Ennis, Tyler', 1, 2014, 2016, 1610612745, 'Y'],
        [201569, 'Gordon, Eric', 1, 2008, 2016, 1610612745, 'Y'],
        [201935, 'Harden, James', 1, 2009, 2016, 1610612745, 'Y'],
        [1626149, 'Harrell, Montrezl', 1, 2015, 2016, 1610612745, 'Y'],
        [2403, 'Nene', 1, 2002, 2016, 1610612745, 'Y'],
        [203909, 'McDaniels, KJ', 1, 2014, 2016, 1610612745, 'Y'],
        [1627778, 'Onuaku, Chinanu', 1, 2016, 2016, 1610612745, 'Y'],
        [1627787, 'Wiltjer, Kyle', 1, 2016, 2016, 1610612745, 'Y']
    ],
    1610612746: [
        [101187, 'Anderson, Alan', 1, 2005, 2016, 1610612746, 'Y'],
        [101138, 'Bass, Brandon', 1, 2005, 2016, 1610612746, 'Y'],
        [2037, 'Crawford, Jamal', 1, 2000, 2016, 1610612746, 'Y'],
        [101109, 'Felton, Raymond', 1, 2005, 2016, 1610612746, 'Y'],
        [201933, 'Griffin, Blake', 1, 2009, 2016, 1610612746, 'Y'],
        [1627744, 'Johnson, Brice', 1, 2016, 2016, 1610612746, 'Y'],
        [202325, 'Johnson, Wesley', 1, 2010, 2016, 1610612746, 'Y'],
        [201599, 'Jordan, DeAndre', 1, 2008, 2016, 1610612746, 'Y'],
        [201601, 'Mbah a Moute, Luc', 1, 2008, 2016, 1610612746, 'Y'],
        [101108, 'Paul, Chris', 1, 2005, 2016, 1610612746, 'Y'],
        [1718, 'Pierce, Paul', 1, 1998, 2016, 1610612746, 'Y'],
        [200755, 'Redick, JJ', 1, 2006, 2016, 1610612746, 'Y'],
        [203085, 'Rivers, Austin', 1, 2012, 2016, 1610612746, 'Y'],
        [201578, 'Speights, Marreese', 1, 2008, 2016, 1610612746, 'Y'],
        [1627754, 'Stone, Diamond', 1, 2016, 2016, 1610612746, 'Y']
    ],
    1610612747: [
        [204028, 'Black, Tarik', 1, 2014, 2016, 1610612747, 'Y'],
        [101181, 'Calderon, Jose', 1, 2005, 2016, 1610612747, 'Y'],
        [203903, 'Clarkson, Jordan', 1, 2014, 2016, 1610612747, 'Y'],
        [2736, 'Deng, Luol', 1, 2004, 2016, 1610612747, 'Y'],
        [1626273, 'Huertas, Marcelo', 1, 2015, 2016, 1610612747, 'Y'],
        [1627742, 'Ingram, Brandon', 1, 2016, 2016, 1610612747, 'Y'],
        [202389, 'Mozgov, Timofey', 1, 2010, 2016, 1610612747, 'Y'],
        [1626204, 'Nance Jr., Larry', 1, 2015, 2016, 1610612747, 'Y'],
        [203944, 'Randle, Julius', 1, 2014, 2016, 1610612747, 'Y'],
        [203080, 'Robinson, Thomas', 1, 2012, 2016, 1610612747, 'Y'],
        [1626156, "Russell, D'Angelo", 1, 2015, 2016, 1610612747, 'Y'],
        [101150, 'Williams, Lou', 1, 2005, 2016, 1610612747, 'Y'],
        [1897, 'World Peace, Metta', 1, 1999, 2016, 1610612747, 'Y'],
        [201156, 'Young, Nick', 1, 2007, 2016, 1610612747, 'Y'],
        [1627826, 'Zubac, Ivica', 1, 2016, 2016, 1610612747, 'Y']
    ],
    1610612748: [
        [202337, 'Babbitt, Luke', 1, 2010, 2016, 1610612748, 'Y'],
        [2547, 'Bosh, Chris', 1, 2003, 2016, 1610612748, 'Y'],
        [201609, 'Dragic, Goran', 1, 2008, 2016, 1610612748, 'Y'],
        [201961, 'Ellington, Wayne', 1, 2009, 2016, 1610612748, 'Y'],
        [2617, 'Haslem, Udonis', 1, 2003, 2016, 1610612748, 'Y'],
        [201949, 'Johnson, James', 1, 2009, 2016, 1610612748, 'Y'],
        [204020, 'Johnson, Tyler', 1, 2014, 2016, 1610612748, 'Y'],
        [203585, 'McGruder, Rodney', 1, 2016, 2016, 1610612748, 'Y'],
        [201177, 'McRoberts, Josh', 1, 2007, 2016, 1610612748, 'Y'],
        [203186, 'Reed, Willie', 1, 2012, 2016, 1610612748, 'Y'],
        [1626196, 'Richardson, Josh', 1, 2015, 2016, 1610612748, 'Y'],
        [203079, 'Waiters, Dion', 1, 2012, 2016, 1610612748, 'Y'],
        [202355, 'Whiteside, Hassan', 1, 2010, 2016, 1610612748, 'Y'],
        [202682, 'Williams, Derrick', 1, 2011, 2016, 1610612748, 'Y'],
        [1626159, 'Winslow, Justise', 1, 2015, 2016, 1610612748, 'Y']
    ],
    1610612749: [
        [203507, 'Antetokounmpo, Giannis', 1, 2013, 2016, 1610612749, 'Y'],
        [201563, 'Beasley, Michael', 1, 2008, 2016, 1610612749, 'Y'],
        [1627763, 'Brogdon, Malcolm', 1, 2016, 2016, 1610612749, 'Y'],
        [203521, 'Dellavedova, Matthew', 1, 2013, 2016, 1610612749, 'Y'],
        [203089, 'Henson, John', 1, 2012, 2016, 1610612749, 'Y'],
        [1627748, 'Maker, Thon', 1, 2016, 2016, 1610612749, 'Y'],
        [203114, 'Middleton, Khris', 1, 2012, 2016, 1610612749, 'Y'],
        [202328, 'Monroe, Greg', 1, 2010, 2016, 1610612749, 'Y'],
        [200779, 'Novak, Steve', 1, 2006, 2016, 1610612749, 'Y'],
        [203953, 'Parker, Jabari', 1, 2014, 2016, 1610612749, 'Y'],
        [203101, 'Plumlee, Miles', 1, 2012, 2016, 1610612749, 'Y'],
        [203503, 'Snell, Tony', 1, 2013, 2016, 1610612749, 'Y'],
        [203141, 'Teletovic, Mirza', 1, 2012, 2016, 1610612749, 'Y'],
        [1891, 'Terry, Jason', 1, 1999, 2016, 1610612749, 'Y'],
        [1626173, 'Vaughn, Rashad', 1, 2015, 2016, 1610612749, 'Y']
    ],
    1610612750: [
        [202332, 'Aldrich, Cole', 1, 2010, 2016, 1610612750, 'Y'],
        [202357, 'Bjelica, Nemanja', 1, 2015, 2016, 1610612750, 'Y'],
        [203476, 'Dieng, Gorgui', 1, 2013, 2016, 1610612750, 'Y'],
        [1627739, 'Dunn, Kris', 1, 2016, 2016, 1610612750, 'Y'],
        [201941, 'Hill, Jordan', 1, 2009, 2016, 1610612750, 'Y'],
        [1626145, 'Jones, Tyus', 1, 2015, 2016, 1610612750, 'Y'],
        [203897, 'LaVine, Zach', 1, 2014, 2016, 1610612750, 'Y'],
        [101249, 'Lucas III, John', 1, 2005, 2016, 1610612750, 'Y'],
        [203498, 'Muhammad, Shabazz', 1, 2013, 2016, 1610612750, 'Y'],
        [203940, 'Payne, Adreian', 1, 2014, 2016, 1610612750, 'Y'],
        [201593, 'Pekovic, Nikola', 1, 2010, 2016, 1610612750, 'Y'],
        [201937, 'Rubio, Ricky', 1, 2011, 2016, 1610612750, 'Y'],
        [201575, 'Rush, Brandon', 1, 2008, 2016, 1610612750, 'Y'],
        [1626157, 'Towns, Karl-Anthony', 1, 2015, 2016, 1610612750, 'Y'],
        [203952, 'Wiggins, Andrew', 1, 2014, 2016, 1610612750, 'Y']
    ],
    1610612751: [
        [203461, 'Bennett, Anthony', 1, 2013, 2016, 1610612751, 'Y'],
        [202711, 'Bogdanovic, Bojan', 1, 2014, 2016, 1610612751, 'Y'],
        [202344, 'Booker, Trevor', 1, 2010, 2016, 1610612751, 'Y'],
        [203915, 'Dinwiddie, Spencer', 1, 2014, 2016, 1610612751, 'Y'],
        [1627812, 'Ferrell, Yogi', 1, 2016, 2016, 1610612751, 'Y'],
        [200751, 'Foye, Randy', 1, 2006, 2016, 1610612751, 'Y'],
        [203120, 'Hamilton, Justin', 1, 2013, 2016, 1610612751, 'Y'],
        [203925, 'Harris, Joe', 1, 2014, 2016, 1610612751, 'Y'],
        [1626178, 'Hollis-Jefferson, Rondae', 1, 2015, 2016, 1610612751, 'Y'],
        [203930, 'Kilpatrick, Sean', 1, 2014, 2016, 1610612751, 'Y'],
        [1627747, 'LeVert, Caris', 1, 2016, 2016, 1610612751, 'Y'],
        [202391, 'Lin, Jeremy', 1, 2010, 2016, 1610612751, 'Y'],
        [201572, 'Lopez, Brook', 1, 2008, 2016, 1610612751, 'Y'],
        [1626191, 'McCullough, Chris', 1, 2015, 2016, 1610612751, 'Y'],
        [2449, 'Scola, Luis', 1, 2007, 2016, 1610612751, 'Y'],
        [1627785, 'Whitehead, Isaiah', 1, 2016, 2016, 1610612751, 'Y']
    ],
    1610612752: [
        [2546, 'Anthony, Carmelo', 1, 2003, 2016, 1610612752, 'Y'],
        [1627758, 'Baker, Ron', 1, 2016, 2016, 1610612752, 'Y'],
        [1626195, 'Hernangomez, Willy', 1, 2016, 2016, 1610612752, 'Y'],
        [203200, 'Holiday, Justin', 1, 2012, 2016, 1610612752, 'Y'],
        [201943, 'Jennings, Brandon', 1, 2009, 2016, 1610612752, 'Y'],
        [1627851, 'Kuzminskas, Mindaugas', 1, 2016, 2016, 1610612752, 'Y'],
        [201584, 'Lee, Courtney', 1, 2008, 2016, 1610612752, 'Y'],
        [1626254, 'Ndour, Maurice', 1, 2016, 2016, 1610612752, 'Y'],
        [201149, 'Noah, Joakim', 1, 2007, 2016, 1610612752, 'Y'],
        [203124, "O'Quinn, Kyle", 1, 2012, 2016, 1610612752, 'Y'],
        [1627850, 'Plumlee, Marshall', 1, 2016, 2016, 1610612752, 'Y'],
        [204001, 'Porzingis, Kristaps', 1, 2015, 2016, 1610612752, 'Y'],
        [201565, 'Rose, Derrick', 1, 2008, 2016, 1610612752, 'Y'],
        [202498, 'Thomas, Lance', 1, 2011, 2016, 1610612752, 'Y'],
        [2756, 'Vujacic, Sasha', 1, 2004, 2016, 1610612752, 'Y']
    ],
    1610612753: [
        [201571, 'Augustin, D.J.', 1, 2008, 2016, 1610612753, 'Y'],
        [202687, 'Biyombo, Bismack', 1, 2011, 2016, 1610612753, 'Y'],
        [203095, 'Fournier, Evan', 1, 2012, 2016, 1610612753, 'Y'],
        [203932, 'Gordon, Aaron', 1, 2014, 2016, 1610612753, 'Y'],
        [201145, 'Green, Jeff', 1, 2007, 2016, 1610612753, 'Y'],
        [1626209, 'Hezonja, Mario', 1, 2015, 2016, 1610612753, 'Y'],
        [201586, 'Ibaka, Serge', 1, 2009, 2016, 1610612753, 'Y'],
        [201975, 'Meeks, Jodie', 1, 2009, 2016, 1610612753, 'Y'],
        [202620, 'Onuaku, Arinze', 1, 2013, 2016, 1610612753, 'Y'],
        [203901, 'Payton, Elfrid', 1, 2014, 2016, 1610612753, 'Y'],
        [204014, 'Rudez, Damjan', 1, 2014, 2016, 1610612753, 'Y'],
        [202696, 'Vucevic, Nikola', 1, 2011, 2016, 1610612753, 'Y'],
        [201228, 'Watson, CJ', 1, 2007, 2016, 1610612753, 'Y'],
        [203912, 'Wilcox, CJ', 1, 2014, 2016, 1610612753, 'Y'],
        [1627757, 'Zimmerman, Stephen', 1, 2016, 2016, 1610612753, 'Y']
    ],
    1610612754: [
        [202730, 'Allen, Lavoy', 1, 2011, 2016, 1610612754, 'Y'],
        [201166, 'Brooks, Aaron', 1, 2007, 2016, 1610612754, 'Y'],
        [1626176, 'Christmas, Rakeem', 1, 2015, 2016, 1610612754, 'Y'],
        [101145, 'Ellis, Monta', 1, 2005, 2016, 1610612754, 'Y'],
        [202331, 'George, Paul', 1, 2010, 2016, 1610612754, 'Y'],
        [2744, 'Jefferson, Al', 1, 2004, 2016, 1610612754, 'Y'],
        [101139, 'Miles, CJ', 1, 2005, 2016, 1610612754, 'Y'],
        [1627777, 'Niang, Georges', 1, 2016, 2016, 1610612754, 'Y'],
        [203922, 'Robinson, Glenn', 1, 2014, 2016, 1610612754, 'Y'],
        [202338, 'Seraphin, Kevin', 1, 2010, 2016, 1610612754, 'Y'],
        [201155, 'Stuckey, Rodney', 1, 2007, 2016, 1610612754, 'Y'],
        [201952, 'Teague, Jeff', 1, 2009, 2016, 1610612754, 'Y'],
        [1626167, 'Turner, Myles', 1, 2015, 2016, 1610612754, 'Y'],
        [1626202, 'Young, Joe', 1, 2015, 2016, 1610612754, 'Y'],
        [201152, 'Young, Thaddeus', 1, 2007, 2016, 1610612754, 'Y']
    ],
    1610612755: [
        [201573, 'Bayless, Jerryd', 1, 2008, 2016, 1610612755, 'Y'],
        [203496, 'Covington, Robert', 1, 2013, 2016, 1610612755, 'Y'],
        [203954, 'Embiid, Joel', 1, 2014, 2016, 1610612755, 'Y'],
        [201945, 'Henderson, Gerald', 1, 2009, 2016, 1610612755, 'Y'],
        [1626158, 'Holmes, Richaun', 1, 2015, 2016, 1610612755, 'Y'],
        [101141, 'Ilyasova, Ersan', 1, 2006, 2016, 1610612755, 'Y'],
        [1627789, 'Luwawu-Cabarrot, Timothe', 1, 2016, 2016, 1610612755, 'Y'],
        [204456, 'McConnell, TJ', 1, 2015, 2016, 1610612755, 'Y'],
        [203457, 'Noel, Nerlens', 1, 2013, 2016, 1610612755, 'Y'],
        [1626143, 'Okafor, Jahlil', 1, 2015, 2016, 1610612755, 'Y'],
        [200771, 'Rodriguez, Sergio', 1, 2006, 2016, 1610612755, 'Y'],
        [203967, 'Saric, Dario', 1, 2016, 2016, 1610612755, 'Y'],
        [1627732, 'Simmons, Ben', 1, 2016, 2016, 1610612755, 'N'],
        [203917, 'Stauskas, Nik', 1, 2014, 2016, 1610612755, 'Y'],
        [203138, 'Thompson, Hollis', 1, 2013, 2016, 1610612755, 'Y']
    ],
    1610612756: [
        [2571, 'Barbosa, Leandro', 1, 2003, 2016, 1610612756, 'Y'],
        [1627733, 'Bender, Dragan', 1, 2016, 2016, 1610612756, 'Y'],
        [202339, 'Bledsoe, Eric', 1, 2010, 2016, 1610612756, 'Y'],
        [1626164, 'Booker, Devin', 1, 2015, 2016, 1610612756, 'Y'],
        [2199, 'Chandler, Tyson', 1, 2001, 2016, 1610612756, 'Y'],
        [1627737, 'Chriss, Marquese', 1, 2016, 2016, 1610612756, 'Y'],
        [201162, 'Dudley, Jared', 1, 2007, 2016, 1610612756, 'Y'],
        [203098, 'Jenkins, John', 1, 2012, 2016, 1610612756, 'Y'],
        [1627884, 'Jones, Jr., Derrick', 1, 2016, 2016, 1610612756, 'Y'],
        [202688, 'Knight, Brandon', 1, 2011, 2016, 1610612756, 'Y'],
        [203458, 'Len, Alex', 1, 2013, 2016, 1610612756, 'Y'],
        [200782, 'Tucker, PJ', 1, 2006, 2016, 1610612756, 'Y'],
        [1627755, 'Ulis, Tyler', 1, 2016, 2016, 1610612756, 'Y'],
        [203933, 'Warren, TJ', 1, 2014, 2016, 1610612756, 'Y'],
        [1626210, 'Williams, Alan', 1, 2015, 2016, 1610612756, 'Y']
    ],
    1610612757: [
        [202329, 'Aminu, Al-Farouq', 1, 2010, 2016, 1610612757, 'Y'],
        [1626192, 'Connaughton, Pat', 1, 2015, 2016, 1610612757, 'Y'],
        [203459, 'Crabbe, Allen', 1, 2013, 2016, 1610612757, 'Y'],
        [202334, 'Davis, Ed', 1, 2010, 2016, 1610612757, 'Y'],
        [203105, 'Ezeli, Festus', 1, 2012, 2016, 1610612757, 'Y'],
        [203090, 'Harkless, Maurice', 1, 2012, 2016, 1610612757, 'Y'],
        [1627774, 'Layman, Jake', 1, 2016, 2016, 1610612757, 'Y'],
        [203086, 'Leonard, Meyers', 1, 2012, 2016, 1610612757, 'Y'],
        [203081, 'Lillard, Damian', 1, 2012, 2016, 1610612757, 'Y'],
        [203468, 'McCollum, CJ', 1, 2013, 2016, 1610612757, 'Y'],
        [203894, 'Napier, Shabazz', 1, 2014, 2016, 1610612757, 'Y'],
        [203486, 'Plumlee, Mason', 1, 2013, 2016, 1610612757, 'Y'],
        [1627817, 'Quarterman, Tim', 1, 2016, 2016, 1610612757, 'Y'],
        [202323, 'Turner, Evan', 1, 2010, 2016, 1610612757, 'Y'],
        [203943, 'Vonleh, Noah', 1, 2014, 2016, 1610612757, 'Y']
    ],
    1610612758: [
        [201167, 'Afflalo, Arron', 1, 2007, 2016, 1610612758, 'Y'],
        [2440, 'Barnes, Matt', 1, 2002, 2016, 1610612758, 'Y'],
        [201956, 'Casspi, Omri', 1, 2009, 2016, 1610612758, 'Y'],
        [1626161, 'Cauley-Stein, Willie', 1, 2015, 2016, 1610612758, 'Y'],
        [201954, 'Collison, Darren', 1, 2009, 2016, 1610612758, 'Y'],
        [202326, 'Cousins, DeMarcus', 1, 2010, 2016, 1610612758, 'Y'],
        [200752, 'Gay, Rudy', 1, 2006, 2016, 1610612758, 'Y'],
        [201585, 'Koufos, Kosta', 1, 2008, 2016, 1610612758, 'Y'],
        [1627746, 'Labissiere, Skal', 1, 2016, 2016, 1610612758, 'Y'],
        [201951, 'Lawson, Ty', 1, 2009, 2016, 1610612758, 'Y'],
        [203463, 'McLemore, Ben', 1, 2013, 2016, 1610612758, 'Y'],
        [1627834, 'Papagiannis, Georgios', 1, 2016, 2016, 1610612758, 'Y'],
        [1627781, 'Richardson, Malachi', 1, 2016, 2016, 1610612758, 'Y'],
        [202066, 'Temple, Garrett', 1, 2009, 2016, 1610612758, 'Y'],
        [201229, 'Tolliver, Anthony', 1, 2008, 2016, 1610612758, 'Y']
    ],
    1610612759: [
        [200746, 'Aldridge, LaMarcus', 1, 2006, 2016, 1610612759, 'Y'],
        [203937, 'Anderson, Kyle', 1, 2014, 2016, 1610612759, 'Y'],
        [202722, 'Bertans, Davis', 1, 2016, 2016, 1610612759, 'Y'],
        [203473, 'Dedmon, Dewayne', 1, 2013, 2016, 1610612759, 'Y'],
        [1627854, 'Forbes, Bryn', 1, 2016, 2016, 1610612759, 'Y'],
        [2200, 'Gasol, Pau', 1, 2001, 2016, 1610612759, 'Y'],
        [1938, 'Ginobili, Manu', 1, 2002, 2016, 1610612759, 'Y'],
        [201980, 'Green, Danny', 1, 2009, 2016, 1610612759, 'Y'],
        [1627879, 'Laprovittola, Nicolas', 1, 2016, 2016, 1610612759, 'Y'],
        [101135, 'Lee, David', 1, 2005, 2016, 1610612759, 'Y'],
        [202695, 'Leonard, Kawhi', 1, 2011, 2016, 1610612759, 'Y'],
        [201988, 'Mills, Patty', 1, 2009, 2016, 1610612759, 'Y'],
        [1627749, 'Murray, Dejounte', 1, 2016, 2016, 1610612759, 'Y'],
        [2225, 'Parker, Tony', 1, 2001, 2016, 1610612759, 'Y'],
        [203613, 'Simmons, Jonathon', 1, 2015, 2016, 1610612759, 'Y']
    ],
    1610612760: [
        [203518, 'Abrines, Alex', 1, 2016, 2016, 1610612760, 'Y'],
        [203500, 'Adams, Steven', 1, 2013, 2016, 1610612760, 'Y'],
        [203902, 'Christon, Semaj', 1, 2016, 2016, 1610612760, 'Y'],
        [2555, 'Collison, Nick', 1, 2003, 2016, 1610612760, 'Y'],
        [203924, 'Grant, Jerami', 1, 2014, 2016, 1610612760, 'Y'],
        [203962, 'Huestis, Josh', 1, 2015, 2016, 1610612760, 'Y'],
        [202683, 'Kanter, Enes', 1, 2011, 2016, 1610612760, 'Y'],
        [203530, 'Lauvergne, Joffrey', 1, 2014, 2016, 1610612760, 'Y'],
        [201627, 'Morrow, Anthony', 1, 2008, 2016, 1610612760, 'Y'],
        [203506, 'Oladipo, Victor', 1, 2013, 2016, 1610612760, 'Y'],
        [1626166, 'Payne, Cameron', 1, 2015, 2016, 1610612760, 'Y'],
        [203460, 'Roberson, Andre', 1, 2013, 2016, 1610612760, 'Y'],
        [1627734, 'Sabonis, Domantas', 1, 2016, 2016, 1610612760, 'Y'],
        [202713, 'Singler, Kyle', 1, 2012, 2016, 1610612760, 'Y'],
        [201566, 'Westbrook, Russell', 1, 2008, 2016, 1610612760, 'Y']
    ],
    1610612761: [
        [203998, 'Caboclo, Bruno', 1, 2014, 2016, 1610612761, 'Y'],
        [201960, 'Carroll, DeMarre', 1, 2009, 2016, 1610612761, 'Y'],
        [201942, 'DeRozan, DeMar', 1, 2009, 2016, 1610612761, 'Y'],
        [202709, 'Joseph, Cory', 1, 2011, 2016, 1610612761, 'Y'],
        [200768, 'Lowry, Kyle', 1, 2006, 2016, 1610612761, 'Y'],
        [203512, 'Nogueira, Lucas', 1, 2014, 2016, 1610612761, 'Y'],
        [202335, 'Patterson, Patrick', 1, 2010, 2016, 1610612761, 'Y'],
        [1627751, 'Poeltl, Jakob', 1, 2016, 2016, 1610612761, 'Y'],
        [1626181, 'Powell, Norman', 1, 2015, 2016, 1610612761, 'Y'],
        [203082, 'Ross, Terrence', 1, 2012, 2016, 1610612761, 'Y'],
        [1627783, 'Siakam, Pascal', 1, 2016, 2016, 1610612761, 'Y'],
        [203096, 'Sullinger, Jared', 1, 2012, 2016, 1610612761, 'Y'],
        [202685, 'Valanciunas, Jonas', 1, 2012, 2016, 1610612761, 'Y'],
        [1627832, 'VanVleet, Fred', 1, 2016, 2016, 1610612761, 'Y'],
        [1626153, 'Wright, Delon', 1, 2015, 2016, 1610612761, 'Y']
    ],
    1610612762: [
        [1627762, 'Bolomboy, Joel', 1, 2016, 2016, 1610612762, 'Y'],
        [202692, 'Burks, Alec', 1, 2011, 2016, 1610612762, 'Y'],
        [2564, 'Diaw, Boris', 1, 2003, 2016, 1610612762, 'Y'],
        [203957, 'Exum, Dante', 1, 2014, 2016, 1610612762, 'Y'],
        [202324, 'Favors, Derrick', 1, 2010, 2016, 1610612762, 'Y'],
        [203497, 'Gobert, Rudy', 1, 2013, 2016, 1610612762, 'Y'],
        [202330, 'Hayward, Gordon', 1, 2010, 2016, 1610612762, 'Y'],
        [201588, 'Hill, George', 1, 2008, 2016, 1610612762, 'Y'],
        [203918, 'Hood, Rodney', 1, 2014, 2016, 1610612762, 'Y'],
        [204060, 'Ingles, Joe', 1, 2014, 2016, 1610612762, 'Y'],
        [2207, 'Johnson, Joe', 1, 2001, 2016, 1610612762, 'Y'],
        [1626168, 'Lyles, Trey', 1, 2015, 2016, 1610612762, 'Y'],
        [202714, 'Mack, Shelvin', 1, 2011, 2016, 1610612762, 'Y'],
        [203526, 'Neto, Raul', 1, 2015, 2016, 1610612762, 'Y'],
        [203481, 'Withey, Jeff', 1, 2013, 2016, 1610612762, 'Y']
    ],
    1610612763: [
        [2754, 'Allen, Tony', 1, 2004, 2016, 1610612763, 'Y'],
        [1627735, 'Baldwin IV, Wade', 1, 2016, 2016, 1610612763, 'Y'],
        [1713, 'Carter, Vince', 1, 1998, 2016, 1610612763, 'Y'],
        [201144, 'Conley, Mike', 1, 2007, 2016, 1610612763, 'Y'],
        [203584, 'Daniels, Troy', 1, 2013, 2016, 1610612763, 'Y'],
        [1627738, 'Davis, Deyonta', 1, 2016, 2016, 1610612763, 'Y'],
        [203516, 'Ennis III, James', 1, 2014, 2016, 1610612763, 'Y'],
        [201188, 'Gasol, Marc', 1, 2008, 2016, 1610612763, 'Y'],
        [203210, 'Green, JaMychal', 1, 2014, 2016, 1610612763, 'Y'],
        [1626150, 'Harrison, Andrew', 1, 2016, 2016, 1610612763, 'Y'],
        [1626185, 'Martin, Jarell', 1, 2015, 2016, 1610612763, 'Y'],
        [202718, 'Parsons, Chandler', 1, 2011, 2016, 1610612763, 'Y'],
        [2216, 'Randolph, Zach', 1, 2001, 2016, 1610612763, 'Y'],
        [1627786, 'Williams, Troy', 1, 2016, 2016, 1610612763, 'Y'],
        [201148, 'Wright, Brandan', 1, 2007, 2016, 1610612763, 'Y']
    ],
    1610612764: [
        [203078, 'Beal, Bradley', 1, 2012, 2016, 1610612764, 'Y'],
        [203504, 'Burke, Trey', 1, 2013, 2016, 1610612764, 'Y'],
        [101162, 'Gortat, Marcin', 1, 2007, 2016, 1610612764, 'Y'],
        [1627863, 'House, Danuel', 1, 2016, 2016, 1610612764, 'Y'],
        [101133, 'Mahinmi, Ian', 1, 2007, 2016, 1610612764, 'Y'],
        [1627815, 'McClellan, Sheldon', 1, 2016, 2016, 1610612764, 'Y'],
        [202693, 'Morris, Markieff', 1, 2011, 2016, 1610612764, 'Y'],
        [203094, 'Nicholson, Andrew', 1, 2012, 2016, 1610612764, 'Y'],
        [1627849, 'Ochefu, Daniel', 1, 2016, 2016, 1610612764, 'Y'],
        [1626162, 'Oubre, Kelly', 1, 2015, 2016, 1610612764, 'Y'],
        [203490, 'Porter, Otto', 1, 2013, 2016, 1610612764, 'Y'],
        [203107, 'Satoransky, Tomas', 1, 2016, 2016, 1610612764, 'Y'],
        [201160, 'Smith, Jason', 1, 2007, 2016, 1610612764, 'Y'],
        [201977, 'Thornton, Marcus', 1, 2009, 2016, 1610612764, 'Y'],
        [202322, 'Wall, John', 1, 2010, 2016, 1610612764, 'Y']
    ],
    1610612765: [
        [203382, 'Baynes, Aron', 1, 2012, 2016, 1610612765, 'Y'],
        [203493, 'Bullock, Reggie', 1, 2013, 2016, 1610612765, 'Y'],
        [203484, 'Caldwell-Pope, Kentavious', 1, 2013, 2016, 1610612765, 'Y'],
        [203083, 'Drummond, Andre', 1, 2012, 2016, 1610612765, 'Y'],
        [1627740, 'Ellenson, Henry', 1, 2016, 2016, 1610612765, 'Y'],
        [1627771, 'Gbinije, Michael', 1, 2016, 2016, 1610612765, 'Y'],
        [202699, 'Harris, Tobias', 1, 2011, 2016, 1610612765, 'Y'],
        [1626199, 'Hilliard, Darrun', 1, 2015, 2016, 1610612765, 'Y'],
        [202704, 'Jackson, Reggie', 1, 2011, 2016, 1610612765, 'Y'],
        [1626169, 'Johnson, Stanley', 1, 2015, 2016, 1610612765, 'Y'],
        [202720, 'Leuer, Jon', 1, 2011, 2016, 1610612765, 'Y'],
        [1626246, 'Marjanovic, Boban', 1, 2015, 2016, 1610612765, 'Y'],
        [202694, 'Morris, Marcus', 1, 2011, 2016, 1610612765, 'Y'],
        [202397, 'Smith, Ish', 1, 2010, 2016, 1610612765, 'Y'],
        [2757, 'Udrih, Beno', 1, 2004, 2016, 1610612765, 'Y']
    ],
    1610612766: [
        [201587, 'Batum, Nicolas', 1, 2008, 2016, 1610612766, 'Y'],
        [201158, 'Belinelli, Marco', 1, 2007, 2016, 1610612766, 'Y'],
        [1626203, 'Graham, Treveon', 1, 2016, 2016, 1610612766, 'Y'],
        [1626151, 'Harrison, Aaron', 1, 2015, 2016, 1610612766, 'Y'],
        [201150, 'Hawes, Spencer', 1, 2007, 2016, 1610612766, 'Y'],
        [201579, 'Hibbert, Roy', 1, 2008, 2016, 1610612766, 'Y'],
        [1626163, 'Kaminsky, Frank', 1, 2015, 2016, 1610612766, 'Y'],
        [203077, 'Kidd-Gilchrist, Michael', 1, 2012, 2016, 1610612766, 'Y'],
        [203087, 'Lamb, Jeremy', 1, 2012, 2016, 1610612766, 'Y'],
        [203148, 'Roberts, Brian', 1, 2012, 2016, 1610612766, 'Y'],
        [201196, 'Sessions, Ramon', 1, 2007, 2016, 1610612766, 'Y'],
        [202689, 'Walker, Kemba', 1, 2011, 2016, 1610612766, 'Y'],
        [101107, 'Williams, Marvin', 1, 2005, 2016, 1610612766, 'Y'],
        [1626174, 'Wood, Christian', 1, 2015, 2016, 1610612766, 'Y'],
        [203469, 'Zeller, Cody', 1, 2013, 2016, 1610612766, 'Y']
    ]
}