    #1) In CSS "#" is uses for targeting the id for edit and "." is uses for targeting class for edit

#1.1) background color use for background color while only colour is uses for font colour

#2) In css There are 3 methods for using style..
     i) Inline method :- use style tag directly on the line before closing id,class or whatever which is required
     ii) Internal Method:- use style before the closing of head tag or after the title tag and use "#" or "." according the requirement
     iii) External method:- use link tag before the closing of head tag and create any CSS file
     
#3) Selectors In CSS:-
     i)Body Selector:- In this we use body keyword  which is uses in style section which is under the link section .. in this entire code's heading or paragaphs can be selected at a time for applyting properties of Cascading style Sheet
     ii)Element Selector:-In this selecto we select an element like Heading, or paragraph then apple CSS properties at a single element
     iii)Id Selector:- This selector is uses for select an Id using "#" and apply CSS Properties in this perticular ID
     iv)Class Selector:- This selectoe is uses for select and class using "." and apply all the CSS properties on it.
     v) Universal Selector:- by using "*" we can access changes in properties in entire body
     
#3) P.red or P#red command is uses for entire red color to all paragraphs of class or id
     
#4) */ ....*/ is uses for commenting in CSS
     
#5) Ek element me ek se jyada class ho skti h ya ek class me ek se jyada elements ho skte h lekin id k case me hr element ki ek unique id hoti h ya bol skteh ki hr element ki apni ek id hoti h jo ki unique hoti h or ek se jyada nhi hoti h
     
#6) Inline method having more priority as compare to INTERNAL & EXTERNAL method of CSS

#6.1) DIV is by default a BLOCK ELEMENT while spane is by default an INLINE ELEMENT    
     
                          """ Chap - 2 """
                          
#7) HSL stands for Hue, Saturation & Lightness

#8) Insertion of any image in background can be easily done by "background image: url('NAME OF IMAGE FROM OPEN FOLDER')

#9) "background image: url('NAME OF IMAGE FROM OPEN FOLDER')

Background-repeat: repeat-x; { only repeats along the x axis not in y axis )
Background-repeat: repeat-y; { only repeats along the y axis not in x axis )
Background-repeat: no repeat
background-repeat: space; ( Image will be repeat alng the x-axis without cutting any image. All the images will be completely prresent
background-size: cover; ( Image will be display on the entire screen no any space will remaining )
background-size: contain; ( try to visible full image )
""" Cover me koi jgn nhi bchati qki puri space required hoti h jbki contain me according to height and weight space will remain in image and uski jgh extra box show hota h """
background-size: auto; will cover the image according to given heights & width
background-position: left top {THis command puts background accoding to box'x Heights and width in top,bottom.center.left-top,bottom-right}
background-attachment: scroll; by this command background will also get scrolled with written paragraph
background-attachment: fixed; by this background will e fixed and only paragraph or text will be scrolled
background-size:- (width,height) will change the height and width of background    while in div style section width and height stads for entire div section's dimensions

                          """ Chap - 3 """
                               
#10) in flexbox:- MBPC:- Marign , Border , Padding , Content
margin:- Inserted content ki ceiling se ya web page me kitni distance se niche h..margin hota h
Border:- Thinkness of border inside this Border section is represents
padding:- Inserted content ki insrted border waali ceiling se kitni distance h ..padding khlaata h

Syntax of MARGIN is given as: Apx,Bpx,cpx,Dpx      -     Top,Right,Bottom,Left
                            
and when any two values are given.. then syntax behaves as: Apx,Bpx .... Top-bottom,right-left
                            
Syntax of Border is given as :- width,style,color
Border Radius:- is uses for change in the shape of border from each corner as wll as in terms of each side

Margin Collapse:- iN this agar 2 boxes he to upr waale box ki margin or niche waale box ki margin same h to to dono ki apni apni utni hi length ki margins hogi lekin yadi upr waale box or niche waale box ki margin alg h to jiski margin km h vo jyaada waali margin ke saath overlap ho jayegi
                  This concept is known as MARGIN COLLAPSE.
Box Sizing:- is total size of box on the basis of sum of both margins(top & bottom), sum of both paddings,sum of border size, sum of inserted height
Box Sizing and Content Box both are equal
                            
In Border Box Padding and Border both are include in width..

Contain box me kvl width and height included hote h jbki border box me padding and border bhi shaamil hote h
                               

                          """ Chap - 4 """

#11) Display and its properties:-
Display-Inline:- Only takes space which is required by written text.. not more than this.
                 In case of display inline property HEIGHT & WIDTH doesn't affect.
                 and in case of MARGIN & PADDING it will ONLY ALLOWS   for left & right   NOT for            top and bottom
                               { Inline ko Height or weight se koi frk nhi pdhta vh apna size utna hi rkhega jitna accoding to text required h Margin or padding s frk pdhta h pr kevl left & right k case me top & bottom k case me nhi }
                  
Display Block:- In this we can set WIDTH & HEIGHT  and Margin & padding according to our reuirement

Display INLINE_BLOCK:- as we know in case of inline element we cannot set width and height and MArgin as well as Padding..but still we want to set WIDTH & HEIGHT & MARGIN & PADDING in case of INLINE element then in this case we use DISPLAY INLINE BLOCK property

Display None :-  is the option uses for remove diplay ..matlab uski jgh or kuchh or aa skta h

Visibility Hidden:- In this option it will only disappear not removed from their that's why other element will not able to take place of this element.Vo kevl hide hua h lekin he vhi pr isliye vha pr koi dusra element aa skta h
                             
TextAlign:- uses for align the text from left,right, top and bottom center etc places.                            

TextDecoration Property:- This property apply all the decoration work for the text.. we can underline text,change underline shape,size and color

Line-height:- this is uses for specify line's height in paragraph among several lines

font-size:- uses for change in the size of font

font-family:- is uses for change or edit the fontface of font If there is space in name of font then we use desh(') otherwise font name can be written directly without desh(')
               In font family when link is not available from google on copied then select from font family section and use in the code
font Weight- property stands for thickness or bold font face. Which varies from thin to thick

font-family:- stands for fixed font family as "Times Nw Roman" etc
Generic-famiy:- stands for any particular font we can use here ( Broad Group of fonts )


                          """ Chap - 5 """

# What is Responsive Website..?
Ans:- a website that can be easily open from anywhere in anydevice. This website changes his pattern according to different different device.
# Units in Fonts:-
1)em:- (My Parent element) font size in "em" indicates the  font size "n" times of parental font size
2)rem:- (Root Font Size) font size will be "n" times of "HTML TAG" or "HTML ELEMENT SIZE"
3)vw:- user ki screen ka 1% stnads for view width. Different screen for different different devices. If 50vw then 50% of users view width
4)vh:- user ki screen ka 1% stands for view height. Different screen for differenr different devices, If 50vh of 50% of users view height

1)min-height: 50vh :- km se km height iski 50% to hona hi chahiye entire screen ki..  isse jyada according to user set ki ja skti h
2)max-height: 50vh:- max to max height 50% ho skti h..web page ki isse km kuchhho skti h baaki at max to itni hi hogi
3)min-width : 50vh :- Min width 50% of entire screen to honi hi chahiye isse jyada user apne according set kr skta h lekin itni to honi hi chahiye..
4)max-height: 50vh:- max to max width 50% ho skti h..web page ki isse km to chlega lekin isse jyada nhi hona chahiye

Possition Properties:-
1) Static:- Iss Property me jo h vh hoga by default no any other effect..like top, bottom, left & right..
2) Relative: - Iss property se box ko relatively top,bottom,left and right move kiya ja skta h according to our need. isme kevel jo particular selected box h vo move hota h ..uske aage piche ka koi dusra box nhi..agr jo box move kr rhe h uske noche b box h to kvl moved box move krega dusre nhi
3) Absolute:- Apne phle non-static ancestor ki trph move krega.
4) Fixed:- Iss option se apna box usi position pr stay rhega...bhle hi body kitni bhi vast q nhi ho..ya body ki height kitni b q nhi ho
5) Z-Index:- Jiski bhi Z-index jitni jyada hogi vh utna hi upr rhega..jse if there are two boxes let they have z-index 1 & 3 respectively then by default box 2 will appear upr ki trph 
6) Sticky:- is that condition in which on scrolling selected box or object should stay there and not scrolled. Sticky me particular box scroll nhi hota or vhi pr hang (stick) hota h

List Style Property:- list-style: square inside/outside url('image.jpg') In outside:- image or bullet points will apear outside of ul section(margin) and in INSIDE it will apear similarly inside od ul or margin
""" nvw command is responsible for responsive website where "n" stands for size of the page"""s


                        """ Chap - 6 """
                        
Float:- This is uses for put two block level elements in different directions .. yadi do block level elements ek k niche ek h to ek ko float krne pr dusra uske opposite direction me presenet ho jayega and yadi dono ko same direction me float kiya to dono line me hi parallely ho jayenge
Clear Property:- uses for clear float. In this clear RIGHT can be used and clear all exist

                                            # flex-Container Properties:- .....
                                            
Flex-Direction:- is a property of flexbox uses for assign the direction of all flex boxes.
                :Column - by using thse all flexboxes will me arrange columnwise from "top to bottom"
                
                :Row - by isng these all flexboxes will arrange in row from "left to right"
                
                :Row-Reverse property arranges all the flexboxes from "right to left"
                
                :Column-Reverse - by using these all flexboxes will arranges columwiese from "bottom to top approch"
                
flex-wrap:-  is a property uses when we move our curson for resizing browsers window then all flex boxes are in same order but not rearranged. 
             ( jb cursor se browser ki window ko chhota kiya jata h to saare flexbox vse hi rhte h bus size window k according change hota h lekin rearrange nhi hote..yh ktne k  liye flex-wrap use krte h ..which wraps flexboxes according to browser decremenr or increment shape )
             :wrap - by using these all flexboxes will get wrap as in existing order like Box - 1, then Box - 2, then Box - 2B...
             
             :wrap-reverse - by using these all the flexboxes will wrap in opposite order like first Box - 2C, then Box - 2B then Box -2 then Box - 1
             
             :no-wrap - by using this flexboxes will not wraps

justify-Content:- This property is used for arrange or justify flexboxes any where. ex:- CENTER is a property uses for put align all flexboxes HORIZONTALLY in center

align-items: center is a property  which arrange items in center VERTICALLY

align-content: Align center me saare flexboxes vertically center me align kiye jaate h and agr wrap h to browser ko resize krne pr inka centralized alignment equal distance or kuchh gap k saath hota h..
               Isliye align-content: center; use krke browse ko resizing krne pr bhi flexboxes me distance nhi rhti or resize ho jaate h
               
                                            # flex-items Properties:- .....

order:- is a property uses for change order of flexboxes in each other

align-self: is a property uses for align the selected or particular or targeted flexbox at another place 
           align-self: flex-end;

flex-grow: uses for increase or decrease width of any particular flexbox
           flex-grow: 1;

           
              """ Chap - 7 """

CSS Grid:- use Display:Grid .. this uses for combining more then 1 columns rowwise together

grid-row-gap: 15px; :- Indicates the gap between columns rowwise

grid-template-columns:- yh property grid me jitne columns h un columns ko further alg alg columns me divide krti h..jese 2 baar auto likha to grid me 2-2 k pairs me columns silimarly agr 3 baar column likha to grid me 3-3 k pair me columns
                        grid-template-columns: auto auto; Auto option apne according columns ki width equally kr k no. of auto, columns me devide krta h
                        grid-template-columns: auto 15px :- auto me value insert krne pr inserted data k according colmn devide hote h

grid-template-rows:- yh property grid me rows ko given data k accordign widthwise set krti h ya auto krne pr no. of time auto k according width set kr k row create krti h                        

grid-gap:- is a shothand property for grid-row-gap and grid-column-gap both ..
            grid-gap: 15px 10px; :- First value stands for ROW & second value is for COLUMNS
            In grid-gap property if we assign a SINGLE VALUE then it is valid for both ROW & COLUMN
            
grid columns:- property is applicable in grid-items, in this we can change representation of columns from any box to any box.
               grid-column:- 1/5:- combine from column -1 to column 5 
grid-rows:- by using grid-row 1 column can be extended till multiple rows

@media screen :- is a concept ..ki yadi meri screen/browser ki width ek particular pixels se km hoti h to web page me change aayega..

@media screen and (max-width: 900px){
            body{
                background-color: green;
            }
        }
# Here in above example if width of browse window is 900 or greater than 900px then it's okk but when browser screen or size or width decreases and reaches less than 900 px then browsers background will become green


                                """ Chap - 8 """

Transform:- is uses for change the shape any box or image or elemnt inserted or used in cascading style sheet
                CSS 2-D Transform method:- 
            transform: translate(34px,39px):- in transform TRANSLATE uses for move forward according to insertd px and move up or down accoding to inserted px alon y-axis
            transform: translate(65px, 57%); another value can also be mentioned in terms of percentage(%)
            
            transform: rotate(45deg); is uses for rotate inserted data according to degree 
            transform: rotate(5.6turn); rotate in terms of turns
            
            transform-origin: center; It transforms for all the operations from center it self or default
            transform-origin: 0; Tranformation operations applied from 0
            
            transform: scaleX(n); THis is  uses for transform particular object along X-axis by width "n" and there is increment in width            
            transform: scaleY(n); THis is  uses for transform particular object along Y-axis by width "n"
            transform: scale(3,7); This will scale(Width increment) along with X & Y axis
            transform: scaleZ(n); THis is  uses for transform particular object along Z-axis by width "n"
            
            transform: skew(5deg,6deg); uses for skew element or element ko hwa me kitne degree pr kis axis k along rkhna h..element ko x and y axis k along kitna tedha kiya gya h
            transform: skewX(5deg); will place\tild the object at 5degree from x axis
            transform: skewY(6deg); will tild object along with Y-axis
           # Transfrom ShortHand Property:-  
            transform: matrix(1,2,3,4,5,6);IS a  kind of Shorthand property which apply all the tranform operations in a single property

             "matrix(scaleX(), skewY(), skewX(), scaleY(), translateX(), translateY())" All the functionalities of transform property in a single matrix property
            
                CSS 3-D Transform method:-

            transform: rotateX(ndeg):- Image or object will rotate along X-Axis with inserted n degree
            transform: rotateY(45deg):- Image or object will rotate along Y-Axis with inserted n degree
            transform: rotateZ(45deg):- Image or object will rotate along Z-Axis with inserted n degree
                
Transition:- .box:hover{  
            width: 50px;
        }       "This will change the width of image to given width when there will be hover an image"

    .box{
            width: 500px;
            transition-property: width;  "we can use all option also for everything like height,size etc"
            transition-duration: 1s;   "kitni der k liye transition apply krna h"            
            transition-timing-function:ease-in-out;  "Kis possition or ktna h ..in ya out ya in and out"
            transition-delay: 2s; "hover krne k kitni der baad transiiton aply hoga"
        }
    "Image pr mouse se hover krne pr use given property me in or out hover krega"
All these properties can be written in a single shorthand property
            transition: width 1s ease-in-out 1s;
            transition: Property,Duration.Timing-Funciton,Delay


Animation:-
        #Format of Animation (Calling Only not applies)
        @keyframes widthanimation { " name of animation given by us }
            from{
                width: 300px;
            }
            to{
                width: 600px;
            }
        }
       #necessary properties for applying animation
        
            animation-name: widthanimation; ("write name of animation which we have given during calling or after @keyframes") 
            animation-duration: 3s; ("Time duration of Animation")
            animation-delay: 1s;    ("Time taken in initialization of animation")
            animation-iteration-count: 3; ("no of times performance of animation again and again")
            animation-direction: reverse; (" Direction of animation - NORMAL simple as default, in REVERSE just opposite of default")
            animation-direction: alternate-reverse;("in case of ALTERNATE REVERSE it will show SIMPLE HARMONIC MOTION ..NORMAL to REVERSE & REVERSE to NORMAL")
            animation-timing-function: ease-in-out; ("In this it shows that how animation will move ..start slow then end fast or start fast and end slow")
    
            # Animation ShortHand Property:-         
"Standard Form :- " animation: name,duration,delay,iteration-count,reverse,ease-in-out
                    animation: widthanimation 3s 1s ease-in 4 alternate-reverse

    "We can also use % to % instead of from to To"
    
                    @keyframes widthanimation2 {
            0% {
                width: 900px;
                height: 450px;
            }
            20% {
                width: 100vw;
                height: 50vh;
            }            
        }

   " E-commerce  Website project "

* During adding GOOGLE FONTS:- link statements HTML me aate h jbki import statement CSS me aata h
* variable also exist in CSS and uses as var() then color name inseted because in CSS var() is uses for inserting color and bg-color


    
                
            





OTHER REMARKABLE POINTS OF CSS:-

# Verticle nav bar bnane k liye items ka display :- inline-grid krte h

                        


                            
                            

                            
                                    

                            
                            

                            
                            








                            
