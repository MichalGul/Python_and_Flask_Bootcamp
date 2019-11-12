var cards = ["ciri.png", "geralt.png", "jaskier.png", "jaskier.png","iorweth.png","triss.png","geralt.png", "yen.png",
 "ciri.png","triss.png", "yen.png", "iorweth.png"];

 //alert(cards[4])

 //console.log(cards)


var c0 = document.getElementById('c0');
var c1 = document.getElementById('c1');
var c2 = document.getElementById('c2');
var c3 = document.getElementById('c3');

var c4 = document.getElementById('c4');
var c5 = document.getElementById('c5');
var c6 = document.getElementById('c6');
var c7 = document.getElementById('c7');

var c8 = document.getElementById('c8');
var c9 = document.getElementById('c9');
var c10 = document.getElementById('c10');
var c11 = document.getElementById('c11');

c0.addEventListener("click", function () { revealCard(0); });
c1.addEventListener("click", function () { revealCard(1); });
c2.addEventListener("click", function () { revealCard(2); });
c3.addEventListener("click", function () { revealCard(3); });

c4.addEventListener("click", function () { revealCard(4); });
c5.addEventListener("click", function () { revealCard(5); });
c6.addEventListener("click", function () { revealCard(6); });
c7.addEventListener("click", function () { revealCard(7); });

c8.addEventListener("click", function () { revealCard(8); });
c9.addEventListener("click", function () { revealCard(9); });
c10.addEventListener("click", function () { revealCard(10); });
c11.addEventListener("click", function () { revealCard(11); });

shuffle(cards)

var oneVisible = false;
var turnCounter = 0;
var visible_nr;
var lock = false
var pairsLeft = 6

 function revealCard(nr)
 {
    var img_path = "url(img/" + cards[nr] + ")";

    if ($('#c' + nr).hasClass("card") && lock == false)
    {
        lock = true

        $('#c' + nr).css("background-image", img_path)
        $('#c' + nr).addClass("cardA")
        $('#c' + nr).removeClass("card")
        
        if (oneVisible == false)
        {
            //first card
            oneVisible = true
            visible_nr = nr
            lock = false
            
        }
        else
        {
            //second card
            if (cards[nr] == cards[visible_nr] )
            {
                setTimeout(function () { hide2Cards(nr, visible_nr), 750} );
                
            }
            else
            {
                setTimeout(function () { restore2Cards(nr, visible_nr)}, 1000 );
            }

            turnCounter++
            $('.score').html("Turn counter: " + turnCounter);
            oneVisible = false
        }
        
    }
     //alert(nr)
 }
 
 function hide2Cards (nr_1, nr_2) 
 {  
    $("#c" + nr_1).css("opacity", '0')
    $("#c" + nr_2).css("opacity", '0')

     pairsLeft--;

     if(pairsLeft == 0)
     {
         $('.board').html('<h1>You win! <br> Done in ' + turnCounter+' turns</h1>')
     }

    lock = false

 }

 function restore2Cards(nr_1, nr_2)
 {
     $('#c' + nr_1).css("background-image", "url(img/karta.png")
     $('#c' + nr_1).addClass("card")
     $('#c' + nr_1).removeClass("cardA")

     $('#c' + nr_2).css("background-image", "url(img/karta.png")
     $('#c' + nr_2).addClass("card")
     $('#c' + nr_2).removeClass("cardA")

     lock = false
 }

function shuffle(array) 
{
    var currentIndex = array.length, temporaryValue, randomIndex;

    // While there remain elements to shuffle...
    while (0 !== currentIndex) 
    {
        // Pick a remaining element...
        randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex -= 1;

        // And swap it with the current element.
        temporaryValue = array[currentIndex];
        array[currentIndex] = array[randomIndex];
        array[randomIndex] = temporaryValue;
    }

    return array;
}