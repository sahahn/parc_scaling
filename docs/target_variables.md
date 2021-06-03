# Continuous Variables

## Standing Height (inches)
--------------------------
DEAP name: anthro_3_height_calc

Standing Height Average (inches): If three measurements were obtained, the two closest measurements will be averaged.
Should the third measurement fall equally between the first two measurements, all three will be averaged.
Calculation: if([anthro_3_height_in] <> '', mean([anthro_1_height_in], [anthro_2_height_in], [anthro_3_height_in]), mean([anthro_1_height_in], [anthro_2_height_in]))

## Waist Circumference (inches)
-------------------
DEAP name: anthro_waist_cm

Instructions:
If necessary, Please adjust or unfold your pants to remove any additional thickness or bunching. 1. Now I'd like you to take your thumbs and find the two pointy bones on the front of your body where a belt might go. Once you find them, trace that bone all the way up to its highest point. (Demonstrate the desired position of the arms. RA can do this to their own body as they're talking, so the participant has more guidance.) 2. Once you find the top part of the bone, keep your fingers there while I place the tape measure across your stomach so it's in line with those points. (RA touches the hip area OVER t-shirt to ensure accuracy of location and places tape measure across stomach in line with participant's fingers.) 3. Please cross your arms, and place your hands on opposite shoulders. Think of giving yourself a hug. I'm now going to reach around you to grab the other end of the tape measure, so that I can get a full measurement of your waist. (Extend the measuring tape around the waist. Take the measurement to the nearest 0.1 cm.)

## Measured Weight (lbs)
--------------------
DEAP name: anthro_weight_calc

Average Measured Weight (lbs):If three measurements were obtained, the two closest measurements will be averaged. Should the third measurement fall equally between the first two measurements, all three will be averaged.
Calculation: if([anthro_weight3_lb] <> '',mean([anthro_weight3_lb],[anthro_weight2_lb],[anthro_weight1_lb]), mean([anthro_weight1_lb],[anthro_weight2_lb]))


## RuleBreak CBCL Syndrome Scale
-------------------------
DEAP name: cbcl_scr_syn_rulebreak_r

RuleBreak CBCL Syndrome Scale (raw score) from ABCD Parent Child Behavior Checklist Scores Aseba (CBCL).


## Parent Age (yrs)
--------------------------
DEAP name: demo_prnt_age_p

ABCD Parent Demographics Survey / pdem02 [Demographics]
How old are you? ¿Qué edad tiene usted?
Provide your age in years. If you reuse to answer please choose "refuse to answer" in what follows below. Proporcione su edad en años. Si no sabe o niega contestar, por favor escoja "no se" o "niego contestar" en lo que sigue abajo. //The following questions are about you or the child's family. // The following questions are about you or the child's family.


## Motor Development
---------------------
DEAP name: devhx_20_motor_dev_p

From ABCD Developmental History Questionnaire / dhx01 [Med History].
Would you say his/her motor development (sitting, crawling, walking) was earlier, average, or later than most other children? /¿Diría usted que su desarrollo motriz (sentarse, gatear, caminar) fue más temprano, igual al promedio o más tardío que el de la mayoría de los niños?
1 = Much earlier/ Mucho más temprano; 2 = Somewhat earlier /Un poco más temprano; 3 = About average /Más o menos igual al promedio; 4 = Somewhat later /Un poco más tardío; 5 = Much later /Mucho más tardío; 999 = Don't know/ No lo sé


## Birth Weight (lbs)
------------------------
DEAP name: devhx_2_birth_wt_lbs_p

in ABCD Developmental History Questionnaire / dhx01 [Med History]
search term: devhx_2_birth_wt_lbs_p - matches alias [Alias: birth_weight_lbs]
Birth weight pounds

## Age (months)
---------------------
DEAP name: interview_age

Age of the participant at the time of their interview.


## Little Man Test Score
---------------------
DEAP name: lmt_scr_perc_correct

in ABCD Little Man Task Summary Scores / lmtp201 [Task Based]
search term: lmt_scr_perc_correct - matches element name
Percentage correct of all 32 presented trial

## MACVS Religion Subscale
---------------------
DEAP name: macvs_ss_r_p

MACVS Religion Subscale, Mean: (mex_american1_p + mex_american6_p + mex_american11_p + mex_american15_p + mex_american20_p + mex_american25_p) + mex_american28_p)/7; Validation: All items must be answered
Knight, G. P., Gonzales N. A., et al. (2010) The Mexican American Cultural Values scales for Adolescents and Adults. J Early Adolesc 30(3): 444-481.

Included questions: 

mex_american1_p:
Tell me how much you believe that . . .One's belief in God gives inner strength and meaning to life./ La creencia en Dios da fuerza interna y significado a la vida.
1 = Not at All /Nada; 2 = A Little /Poquito; 3 = Somewhat /Algo; 4 = Very Much /Bastante; 5 = Completely/ Completamente/ The next statements are about what people may think or believe. Remember, there are no right or wrong answers

mex_american6_p:
Tell me how much you believe that . . .God is first; family is second. / Dios está primero, la familia está segundo.
1 = Not at All /Nada; 2 = A Little /Poquito; 3 = Somewhat /Algo; 4 = Very Much /Bastante; 5 = Completely/ Completamente/ The next statements are about what people may think or believe. Remember, there are no right or wrong answers

mex_american11_p:
Tell me how much you believe that . . .Parents should teach their children how to pray. / Los padres deberían enseñarle a sus hijos a rezar.
1 = Not at All /Nada; 2 = A Little /Poquito; 3 = Somewhat /Algo; 4 = Very Much /Bastante; 5 = Completely/ Completamente/ The next statements are about what people may think or believe. Remember, there are no right or wrong answers

macvs_15_p:
Tell me how much you believe that . . .If everything is taken away, one still has their faith in God. / Si a uno le quitan todo, todavía le queda la fe en Dios.
1 = Not at All /Nada; 2 = A Little /Poquito; 3 = Somewhat /Algo; 4 = Very Much /Bastante; 5 = Completely/ Completamente/ The next statements are about what people may think or believe. Remember, there are no right or wrong answers

macvs_20_p:
Tell me how much you believe that . . .It is important to thank God every day for all one has. / Es importante darle gracias a Dios todos los días por todo lo que tenemos.
1 = Not at All /Nada; 2 = A Little /Poquito; 3 = Somewhat /Algo; 4 = Very Much /Bastante; 5 = Completely/ Completamente/ The next statements are about what people may think or believe. Remember, there are no right or wrong answers

macvs_25_p:
Tell me how much you believe that . . .It is important to follow the Word of God. / Es importante seguir la palabra de Dios.
1 = Not at All /Nada; 2 = A Little /Poquito; 3 = Somewhat /Algo; 4 = Very Much /Bastante; 5 = Completely/ Completamente/ The next statements are about what people may think or believe. Remember, there are no right or wrong answers

macvs_28_p:
Tell me how much you believe that . . .Religion should be an important part of one's life. / La religión debería ser una parte importante de la vida.
1 = Not at All /Nada; 2 = A Little /Poquito; 3 = Somewhat /Algo; 4 = Very Much /Bastante; 5 = Completely/ Completamente/ The next statements are about what people may think or believe. Remember, there are no right or wrong answers

## Neighborhood Safety
---------------------
DEAP name:neighb_phenx_ss_mean_p

abcd_sscep01 [Social Adjustment]
search term: neighb_phenx_ss_mean_p - matches alias
Neighborhood Safety Protocol: Mean of Parent Report, (neighborhood1r_p + neighborhood2r_p + neighborhood3r_p)/3; Validation: No minimum
Echeverria, S. E., Diez-Roux, A. V., et al. (2004) Reliability of self-reported neighborhood characteristics. J Urban Health 81(4): 682-701; Mujahid, M. S., et al. (2007) Assessing the measurement properties of neighborhood scales: from psychometrics to ecometrics. Am J Epidemiol 165(8): 858-67.

Summed Questions:

neighborhood1r_p:
I feel safe walking in my neighborhood, day or night. Me siento seguro(a) caminando por mi vecindario, de día o de noche.
1 = Strongly Disagree /Muy en desacuerdo; 2 = Disagree /En desacuerdo; 3 = Neutral (neither agree nor disagree)/ Neutral (ni de acuerdo ni en desacuerdo); 4 = Agree /De acuerdo; 5 = Strongly Agree/ Muy de acuerdo//The following questions are about your neighborhood. Your neighborhood is the area within about a 20-minute walk (or about a mile) from your home. For each of the statements please indicate whether you strongly agree, agree, neither agree nor disagree, disagree, or strongly disagree

neighborhood2r_p:
Violence is not a problem in my neighborhood./ La violencia no es un problema en mi vecindario.
1 = Strongly Disagree /Muy en desacuerdo; 2 = Disagree /En desacuerdo; 3 = Neutral (neither agree nor disagree)/ Neutral (ni de acuerdo ni en desacuerdo); 4 = Agree /De acuerdo; 5 = Strongly Agree/ Muy de acuerdo//The following questions are about your neighborhood. Your neighborhood is the area within about a 20-minute walk (or about a mile) from your home. For each of the statements please indicate whether you strongly agree, agree, neither agree nor disagree, disagree, or strongly disagree

neighborhood3r_p:
My neighborhood is safe from crime. Mi vecindario está a salvo de la delincuencia.
1 = Strongly Disagree /Muy en desacuerdo; 2 = Disagree /En desacuerdo; 3 = Neutral (neither agree nor disagree)/ Neutral (ni de acuerdo ni en desacuerdo); 4 = Agree /De acuerdo; 5 = Strongly Agree/ Muy de acuerdo//The following questions are about your neighborhood. Your neighborhood is the area within about a 20-minute walk (or about a mile) from your home. For each of the statements please indicate whether you strongly agree, agree, neither agree nor disagree, disagree, or strongly disagree

## NeuroCog PCA1 (general ability)
---------------------
DEAP name: neurocog_pc1.bl

NeuroCog principal component score 1:general ability (baseline value carry forward)

## NeuroCog PCA2 (executive function)
---------------------
DEAP name: neurocog_pc2.bl 

NeuroCog principal component score 2: executive function (baseline value carry forward)

## NeuroCog PCA3 (learning / memory)
---------------------
DEAP name: neurocog_pc3.bl

NeuroCog principal component score 3:learning/memory (baseline value carry forward)

## NIH Card Sort Test
---------------------
DEAP name: nihtbx_cardsort_uncorrected

NIH Toolbox Dimensional Change Card Sort Test Ages 8-11 v2.0 Uncorrected Standard Score

## NIH List Sorting Working Memory Test
---------------------
DEAP name: nihtbx_list_uncorrected

NIH Toolbox List Sorting Working Memory Test Age 7+ v2.0 Uncorrected Standard Score

## NIH Comparison Processing Speed Test
---------------------
DEAP name: nihtbx_pattern_uncorrected 

NIH Toolbox Pattern Comparison Processing Speed Test Age 7+ v2.0 Uncorrected Standard Score

## NIH Picture Vocabulary Test
---------------------
DEAP name: nihtbx_picvocab_uncorrected

NIH Toolbox Picture Vocabulary Test Age 3+ v2.0 Uncorrected Standard Score

## NIH Oral Reading Recognition Test
---------------------
DEAP name: nihtbx_reading_uncorrected

NIH Toolbox Oral Reading Recognition Test Age 3+ v2.0 Uncorrected Standard Score

## WISC Matrix Reasoning Score
---------------------
DEAP name: pea_wiscv_trs

WISC-V Matrix Reasoning Total Raw Score

## Summed Performance Sports Activity
---------------------
DEAP name: None
Internal name: sports_activity_activities_p_performance

Generated as a sum of: sports_activity_activities_p___[0, 23, 24, 25]

Summed Questions:

sports_activity_activities_p___0:
Please indicate whether your child has EVER participated in any of the following sports and activities continuously for 4 months or more (e.g., for a season in sports, or at least four months of lessons, group participation, etc). We will then ask you some follow-up questions about EACH of the sports or activities in which your child has participated. Indique si su niño(a) ha participado ALGUNA VEZ en cualquiera de los siguientes deportes o actividades continuamente por 4 meses o más (por ejemplo, por una temporada de deporte, o al menos 4 meses de lecciones, participación grupal, etc.). Luego le haremos algunas preguntas de seguimiento acerca de CADA UNO de los deportes o actividades en los cuales su niño(a) ha participado. (0, Ballet, Dance)
0 = No; 1 = Yes

sports_activity_activities_p___23:
Please indicate whether your child has EVER participated in any of the following sports and activities continuously for 4 months or more (e.g., for a season in sports, or at least four months of lessons, group participation, etc). We will then ask you some follow-up questions about EACH of the sports or activities in which your child has participated. Indique si su niño(a) ha participado ALGUNA VEZ en cualquiera de los siguientes deportes o actividades continuamente por 4 meses o más (por ejemplo, por una temporada de deporte, o al menos 4 meses de lecciones, participación grupal, etc.). Luego le haremos algunas preguntas de seguimiento acerca de CADA UNO de los deportes o actividades en los cuales su niño(a) ha participado. ( 23,Musical Instrument (Singing, Choir, Guitar, Piano, Drums, Violin, Flute, Band, Rock Band, Orchestra))
0 = No; 1 = Yes

sports_activity_activities_p___24:
Please indicate whether your child has EVER participated in any of the following sports and activities continuously for 4 months or more (e.g., for a season in sports, or at least four months of lessons, group participation, etc). We will then ask you some follow-up questions about EACH of the sports or activities in which your child has participated. Indique si su niño(a) ha participado ALGUNA VEZ en cualquiera de los siguientes deportes o actividades continuamente por 4 meses o más (por ejemplo, por una temporada de deporte, o al menos 4 meses de lecciones, participación grupal, etc.). Luego le haremos algunas preguntas de seguimiento acerca de CADA UNO de los deportes o actividades en los cuales su niño(a) ha participado. (24,Drawing, Painting, Graphic Art, Photography, Pottery, Sculpting)
0 = No; 1 = Yes

sports_activity_activities_p___25:
(r) Please indicate whether your child has EVER participated in any of the following sports and activities continuously for 4 months or more (e.g., for a season in sports, or at least four months of lessons, group participation, etc). We will then ask you some follow-up questions about EACH of the sports or activities in which your child has participated. Indique si su niño(a) ha participado ALGUNA VEZ en cualquiera de los siguientes deportes o actividades continuamente por 4 meses o más (por ejemplo, por una temporada de deporte, o al menos 4 meses de lecciones, participación grupal, etc.). Luego le haremos algunas preguntas de seguimiento acerca de CADA UNO de los deportes o actividades en los cuales su niño(a) ha participado. (25,Drama, Theater, Acting, Film)
0 = No; 1 = Yes


## Summed Team Sports Activity
---------------------
DEAP name: None
Internal name: sports_activity_activities_p_team_sport

Generated as a sum of: sports_activity_activities_p___[1, 2, 4, 5, 7, 11, 12, 15, 21]

Summed Questions:

sports_activity_activities_p___1:
Please indicate whether your child has EVER participated in any of the following sports and activities continuously for 4 months or more (e.g., for a season in sports, or at least four months of lessons, group participation, etc). We will then ask you some follow-up questions about EACH of the sports or activities in which your child has participated. Indique si su niño(a) ha participado ALGUNA VEZ en cualquiera de los siguientes deportes o actividades continuamente por 4 meses o más (por ejemplo, por una temporada de deporte, o al menos 4 meses de lecciones, participación grupal, etc.). Luego le haremos algunas preguntas de seguimiento acerca de CADA UNO de los deportes o actividades en los cuales su niño(a) ha participado. ( 1,Baseball, Softballl)
0 = No; 1 = Yes

sports_activity_activities_p___2:
Please indicate whether your child has EVER participated in any of the following sports and activities continuously for 4 months or more (e.g., for a season in sports, or at least four months of lessons, group participation, etc). We will then ask you some follow-up questions about EACH of the sports or activities in which your child has participated. Indique si su niño(a) ha participado ALGUNA VEZ en cualquiera de los siguientes deportes o actividades continuamente por 4 meses o más (por ejemplo, por una temporada de deporte, o al menos 4 meses de lecciones, participación grupal, etc.). Luego le haremos algunas preguntas de seguimiento acerca de CADA UNO de los deportes o actividades en los cuales su niño(a) ha participado. ( 2, Basketball Básquetbol)
0 = No; 1 = Yes

sports_activity_activities_p___4:
Please indicate whether your child has EVER participated in any of the following sports and activities continuously for 4 months or more (e.g., for a season in sports, or at least four months of lessons, group participation, etc). We will then ask you some follow-up questions about EACH of the sports or activities in which your child has participated. Indique si su niño(a) ha participado ALGUNA VEZ en cualquiera de los siguientes deportes o actividades continuamente por 4 meses o más (por ejemplo, por una temporada de deporte, o al menos 4 meses de lecciones, participación grupal, etc.). Luego le haremos algunas preguntas de seguimiento acerca de CADA UNO de los deportes o actividades en los cuales su niño(a) ha participado. ( 4, Field Hockey Hockey sobre césped)
0 = No; 1 = Yes

sports_activity_activities_p___5:
Please indicate whether your child has EVER participated in any of the following sports and activities continuously for 4 months or more (e.g., for a season in sports, or at least four months of lessons, group participation, etc). We will then ask you some follow-up questions about EACH of the sports or activities in which your child has participated. Indique si su niño(a) ha participado ALGUNA VEZ en cualquiera de los siguientes deportes o actividades continuamente por 4 meses o más (por ejemplo, por una temporada de deporte, o al menos 4 meses de lecciones, participación grupal, etc.). Luego le haremos algunas preguntas de seguimiento acerca de CADA UNO de los deportes o actividades en los cuales su niño(a) ha participado. ( 5, Football Fútbol americano)
0 = No; 1 = Yes

sports_activity_activities_p___7:
Please indicate whether your child has EVER participated in any of the following sports and activities continuously for 4 months or more (e.g., for a season in sports, or at least four months of lessons, group participation, etc). We will then ask you some follow-up questions about EACH of the sports or activities in which your child has participated. Indique si su niño(a) ha participado ALGUNA VEZ en cualquiera de los siguientes deportes o actividades continuamente por 4 meses o más (por ejemplo, por una temporada de deporte, o al menos 4 meses de lecciones, participación grupal, etc.). Luego le haremos algunas preguntas de seguimiento acerca de CADA UNO de los deportes o actividades en los cuales su niño(a) ha participado. ( 7, Ice Hockey Hockey sobre hielo)
0 = No; 1 = Yes

sports_activity_activities_p___11:
Please indicate whether your child has EVER participated in any of the following sports and activities continuously for 4 months or more (e.g., for a season in sports, or at least four months of lessons, group participation, etc). We will then ask you some follow-up questions about EACH of the sports or activities in which your child has participated. Indique si su niño(a) ha participado ALGUNA VEZ en cualquiera de los siguientes deportes o actividades continuamente por 4 meses o más (por ejemplo, por una temporada de deporte, o al menos 4 meses de lecciones, participación grupal, etc.). Luego le haremos algunas preguntas de seguimiento acerca de CADA UNO de los deportes o actividades en los cuales su niño(a) ha participado. ( 11, Lacrosse Lacrosse)
0 = No; 1 = Yes

sports_activity_activities_p___12:
Please indicate whether your child has EVER participated in any of the following sports and activities continuously for 4 months or more (e.g., for a season in sports, or at least four months of lessons, group participation, etc). We will then ask you some follow-up questions about EACH of the sports or activities in which your child has participated. Indique si su niño(a) ha participado ALGUNA VEZ en cualquiera de los siguientes deportes o actividades continuamente por 4 meses o más (por ejemplo, por una temporada de deporte, o al menos 4 meses de lecciones, participación grupal, etc.). Luego le haremos algunas preguntas de seguimiento acerca de CADA UNO de los deportes o actividades en los cuales su niño(a) ha participado. ( 12, Rugby Rugby)
0 = No; 1 = Yes

sports_activity_activities_p___15:
Please indicate whether your child has EVER participated in any of the following sports and activities continuously for 4 months or more (e.g., for a season in sports, or at least four months of lessons, group participation, etc). We will then ask you some follow-up questions about EACH of the sports or activities in which your child has participated. Indique si su niño(a) ha participado ALGUNA VEZ en cualquiera de los siguientes deportes o actividades continuamente por 4 meses o más (por ejemplo, por una temporada de deporte, o al menos 4 meses de lecciones, participación grupal, etc.). Luego le haremos algunas preguntas de seguimiento acerca de CADA UNO de los deportes o actividades en los cuales su niño(a) ha participado. ( 15, Soccer Fútbol soccer)
0 = No; 1 = Yes

sports_activity_activities_p___21:
Please indicate whether your child has EVER participated in any of the following sports and activities continuously for 4 months or more (e.g., for a season in sports, or at least four months of lessons, group participation, etc). We will then ask you some follow-up questions about EACH of the sports or activities in which your child has participated. Indique si su niño(a) ha participado ALGUNA VEZ en cualquiera de los siguientes deportes o actividades continuamente por 4 meses o más (por ejemplo, por una temporada de deporte, o al menos 4 meses de lecciones, participación grupal, etc.). Luego le haremos algunas preguntas de seguimiento acerca de CADA UNO de los deportes o actividades en los cuales su niño(a) ha participado. ( 21, Volleyball Vóleibol)
0 = No; 1 = Yes

----------------------
# Binary Variables

## Speaks Non-English Language
-------------------------------
DEAP Name: accult_phenx_q2_p

in ABCD Parent Acculturation Survey Modified from PhenX (ACC) / pacc01 [Questionnaire]
search term: accult_phenx_q2_p - matches alias
Besides English, do you speak or understand another language or dialect?


## Thought Problems ASR Syndrome Scale
---------------------------------------
DEAP name: asr_scr_thought_r

in ABCD Parent Adult Self Report Scores Aseba (ASR) / abcd_asrs01 [Questionnaire]
search term: asr_scr_thought_r - matches element name
Thought Problems ASR Syndrome Scale (raw score)

## Aggressive CBCL Syndrome Scale
------------------------------------
DEAP name: cbcl_scr_syn_aggressive_r

Aggressive CBCL Syndrome Scale (raw score)

If grater than 4, then set to 1, if less than or equal to 4, set to 0.

## Born Premature
---------------------
DEAP name: devhx_12a_born_premature_p

Was the child born prematurely? /¿Nació el niño o la niña antes de tiempo?
1 = Yes /Sí; 0 = No /No; 999 = Don't know/ No lo sé

## Incubator Days
---------------------
DEAP name: devhx_15_days_incubator_p

For how many days after birth was he/she in an incubator? /¿Cuántos días estuvo su niño(a) en la incubadora después de su nacimiento?
If he/she was never in an incubator, enter "0". Si nunca estuvo en una incubadora, ingrese "0". If you don't know, please choose "don't know" in what follows below Si no sabe, por favor escoja "no se" en lo que sigue abajo.

## Months Breast Feds
---------------------
DEAP name: devhx_18_mnths_breast_fed_p

For how many months was he/she breast fed? /¿Cuántos meses le/la amamantó?
If he/she was not breast fed, enter "0", 1 year = 12 months, 2 years = 24 months, 3 years = 36 months, etc. Si no le/la amamantó, ingrese "0"; 1 año = 12 meses; 2 años = 24 meses; 3 años = 36 meses; etc. If you don't know, please choose "don't know" in what follows below Si no sabe, por favor escoja "no se" en lo que sigue abajo.

## Has Twin
---------------------
DEAP name: devhx_5_twin_p

Does your child have a twin? /¿Su niño(a) tiene un gemelo?
1 = Yes /Sí; 0 = No /No; 999 = Don't know/ No lo sé

## Planned Prgnancy
---------------------
DEAP name: devhx_6_pregnancy_planned_p

Was your pregnancy with this child a planned pregnancy? /Fue su embarazo con este(a) niño(a) un embarazo planeado?
1 = Yes /Sí; 0 = No /No; 999 = Don't know/ No lo sé

## Distress At Birth
---------------------
DEAP name: None
Internal name: devhx_distress_at_birth

Variables representing distress at birth.
Summed variables =
['devhx_14a_blue_birth_p', 'devhx_14b_slow_heart_beat_p', 'devhx_14c_did_not_breathe_p', 'devhx_14d_convulsions_p', 'devhx_14e_jaundice_p', 'devhx_14f_oxygen_p', 'devhx_14g_blood_transfuse_p', 'devhx_14h_rh_incompatible_p']

Summed Questions (before binarization):

devhx_14a_blue_birth_p:
Did he/she have any of the following complications at birth? Blue at birth? /¿Coloración azul (cianosis) al nacer?
1 = Yes /Sí; 0 = No /No; 999 = Don't know/ No lo sé

devhx_14b_slow_heart_beat_p:
Did he/she have any of the following complications at birth? Slow heart beat?/ ¿Frecuencia cardíaca lenta?
1 = Yes /Sí; 0 = No /No; 999 = Don't know/ No lo sé

devhx_14c_did_not_breathe_p:
Did he/she have any of the following complications at birth? Did not breathe at first? /¿No respiró al principio?
1 = Yes /Sí; 0 = No /No; 999 = Don't know/ No lo sé

devhx_14d_convulsions_p:
Did he/she have any of the following complications at birth? Convulsions? /¿Convulsiones?
1 = Yes /Sí; 0 = No /No; 999 = Don't know/ No lo sé

devhx_14e_jaundice_p:
Did he/she have any of the following complications at birth? Jaundice needing treatment? /¿Ictericia que requirió tratamiento?
1 = Yes /Sí; 0 = No /No; 999 = Don't know/ No lo sé

devhx_14f_oxygen_p:
Did he/she have any of the following complications at birth? Required oxygen?/ ¿Requirió oxígeno?
1 = Yes /Sí; 0 = No /No; 999 = Don't know/ No lo sé

devhx_14g_blood_transfuse_p:
Did he/she have any of the following complications at birth? Required blood transfusion? /¿Requirió una transfusión sanguínea?
1 = Yes /Sí; 0 = No /No; 999 = Don't know/ No lo sé

devhx_14h_rh_incompatible_p:
Did he/she have any of the following complications at birth? Rh incompatibility? /¿Incompatibilidad de Rh?
1 = Yes /Sí; 0 = No /No; 999 = Don't know/ No lo sé

If any, set to 1, else set to 0.

## Mother Pregnancy Problems
---------------------
DEAP name: None
Internal name: devhx_mother_probs

Variables representing mother problems.
Summed variables =
['devhx_10a_severe_nausea_p', 'devhx_10b_heavy_bleeding_p',
 'devhx_10c_eclampsia_p', 'devhx_10e_persist_proteinuria_p', 'devhx_10d_gall_bladder_p',
 'devhx_10f_rubella_p', 'devhx_10g_severe_anemia_p', 'devhx_10h_urinary_infections_p',
 'devhx_10i_diabetes_p', 'devhx_10j_high_blood_press_p', 'devhx_10k_problems_placenta_p',
 'devhx_10l_accident_injury_p', 'devhx_10m_other_p']

Summed Questions (before binarization):

devhx_10a_severe_nausea_p:
During the pregnancy with this child, did you/biological mother have any of the following conditions? Severe nausea and vomiting extending past the 6th month or accompanied by weight loss? /¿Náuseas y vómitos severos que continuaron hasta después del 6.º mes de embarazo o que estuvieron acompañados de una pérdida de peso?
1 = Yes /Sí; 0 = No /No; 999 = Don't know/ No lo sé

devhx_10b_heavy_bleeding_p:
During the pregnancy with this child, did you/biological mother have any of the following conditions? Heavy bleeding requiring bed rest or special treatment? /¿Sangrado abundante que requirió reposo en cama o tratamiento especial?
1 = Yes /Sí; 0 = No /No; 999 = Don't know/ No lo sé

devhx_10c_eclampsia_p:
During the pregnancy with this child, did you/biological mother have any of the following conditions? Pre-eclampsia, eclampsia, or toxemia? /¿Pre-eclampsia, eclampsia o toxemia?
1 = Yes /Sí; 0 = No /No; 999 = Don't know/ No lo sé

devhx_10e_persist_proteinuria_p:
During the pregnancy with this child, did you/biological mother have any of the following conditions? Persistent proteinuria? /¿Proteinuria persistente?
1 = Yes /Sí; 0 = No /No; 999 = Don't know/ No lo sé

devhx_10d_gall_bladder_p:
During the pregnancy with this child, did you/biological mother have any of the following conditions? Severe gall bladder attack? /¿Ataque severo de la vesícula biliar?
1 = Yes /Sí; 0 = No /No; 999 = Don't know/ No lo sé

devhx_10f_rubella_p:
During the pregnancy with this child, did you/biological mother have any of the following conditions? Rubella (German measles) during first 3 months of pregnancy? /¿Rubéola (sarampión alemán) durante los primeros 3 meses de embarazo?
1 = Yes /Sí; 0 = No /No; 999 = Don't know/ No lo sé

devhx_10g_severe_anemia_p:
During the pregnancy with this child, did you/biological mother have any of the following conditions? Severe anemia?/¿Anemia grave?
1 = Yes /Sí; 0 = No /No; 999 = Don't know/ No lo sé

devhx_10h_urinary_infections_p:
During the pregnancy with this child, did you/biological mother have any of the following conditions? Urinary tract infections? /¿Infecciones de vías urinarias?
1 = Yes /Sí; 0 = No /No; 999 = Don't know/ No lo sé

devhx_10i_diabetes_p:
During the pregnancy with this child, did you/biological mother have any of the following conditions? Pregnancy-related diabetes?/ ¿Diabetes relacionada con el embarazo?
1 = Yes /Sí; 0 = No /No; 999 = Don't know/ No lo sé

devhx_10j_high_blood_press_p:
During the pregnancy with this child, did you/biological mother have any of the following conditions? Pregnancy-related high blood pressure? /¿Presión arterial alta relacionada con el embarazo?
1 = Yes /Sí; 0 = No /No; 999 = Don't know/ No lo sé

devhx_10k_problems_placenta_p:
During the pregnancy with this child, did you/biological mother have any of the following conditions? Previa, abruptio, or other problems with the placenta? /¿Placenta previa, desprendimiento de placenta u otros problemas con la placenta?
1 = Yes /Sí; 0 = No /No; 999 = Don't know/ No lo sé

devhx_10l_accident_injury_p:
During the pregnancy with this child, did you/biological mother have any of the following conditions? An accident or injury requiring medical care? /¿Un accidente o lesión que requiriera atención médica?
1 = Yes /Sí; 0 = No /No; 999 = Don't know/ No lo sé

devhx_10m_other_p:
During the pregnancy with this child, did you/biological mother have any of the following conditions? Any other conditions requiring medical care? /¿Algún otro padecimiento que requiriera atención médica?
1 = Yes /Sí; 0 = No /No; 999 = Don't know/ No lo sé

If any, set to 1, else set to 0.

## Any Alcohol 
---------------------
DEAP name: None
Internal name: devhx_ss_alcohol_avg_p

Composite of questions related to alcohol
Summed variables ['devhx_ss_8_alcohol_avg_p', 'devhx_ss_9_alcohol_avg_p']

Summed Questions (before binarization):

devhx_ss_8_alcohol_avg_p:
Alcohol? Average drinks per week?
In the Developmental History survey, if "No" was endorsed for use of a substance, the answer for "Average drinks per week?" was stored as missing. Here we have replaced missing with "0".

devhx_ss_9_alcohol_avg_p:
Alcohol? Average drinks per week?
In the Developmental History survey, if "No" was endorsed for use of a substance, the answer for "Average drinks per week?" was stored as missing. Here we have replaced missing with "0".

If greater than 0, set as yes. Otherwise, No.

## Any Marijuana
---------------------
DEAP name: None
Internal name: devhx_ss_marijuana_amt_p

Composite of questions related to marijuana usage.
Summed variables: ['devhx_ss_8_marijuana_amt_p', 'devhx_ss_9_marijuana_amt_p']

Summed Questions:

devhx_ss_8_marijuana_amt_p:
Marijuana? How many times per day?
In the Developmental History survey, if "No" was endorsed for use of a substance, the answer for "How many times per day?" was stored as missing. Here we have replaced missing with "0".

devhx_ss_9_marijuana_amt_p:
Marijuana? How many times per day?
In the Developmental History survey, if "No" was endorsed for use of a substance, the answer for "How many times per day?" was stored as missing. Here we have replaced missing with "0".

If greater than 0, set as yes. Otherwise, No.

##
---------------------
DEAP name: None
Internal name: screentime_week_p

Generated as Generated as 'screentime_1_hours_p' + 'screentime_1_minutes_p' / 60

Questions:

screentime_1_hours_p:
On a typical WEEKDAY, how much TIME does your child spend on a computer, cellphone, tablet, or other electronic device?/ En un DÍA DE SEMANA típico , ¿cuánto TIEMPO pasa su niño(a) usando una computadora, un teléfono celular, una tableta u otro dispositivo electrónico? Hours/ Horas
Please do NOT include time spent on school related work, but do include watching TV, shows or videos, texting or chatting, playing games, or visiting social networking sites (Facebook, Twitter, Instagram). /Favor NO incluya el tiempo que pasa haciendo trabajos relacionados con la escuela, pero sí incluya el tiempo que pasa viendo televisión, programas o videos, enviando mensajes de texto o chateando, jugando videojuegos o visitando sitios de redes sociales (Facebook, Twitter, Instagram).

screentime_1_minutes_p:
On a typical WEEKDAY, how much TIME does your child spend on a computer, cellphone, tablet, or other electronic device?/ En un DÍA DE SEMANA típico , ¿cuánto TIEMPO pasa su niño(a) usando una computadora, un teléfono celular, una tableta u otro dispositivo electrónico? Minutes/ Minutos
Please do NOT include time spent on school related work, but do include watching TV, shows or videos, texting or chatting, playing games, or visiting social networking sites (Facebook, Twitter, Instagram). /Favor NO incluya el tiempo que pasa haciendo trabajos relacionados con la escuela, pero sí incluya el tiempo que pasa viendo televisión, programas o videos, enviando mensajes de texto o chateando, jugando videojuegos o visitando sitios de redes sociales (Facebook, Twitter, Instagram).

## Screen Time Weekend
---------------------
DEAP name: None
Internal name: screentime_weekend_p

Generated as 'screentime_2_hours_p' + 'screentime_2_minutes_p' / 60

Set to 1 if >5, 0 if <= 5.

Questions:

screentime_2_hours_p:
On a typical WEEKEND DAY, how much TIME does your child spend on a computer, cellphone, tablet, or other electronic device?/ En un típico DIA DE FIN DE SEMANA, ¿cuánto TIEMPO pasa su niño(a) usando una computadora, un teléfono celular, una tableta u otro dispositivo electrónico? Hours/ Horas
Please do NOT include time spent on school related work, but do include watching TV, shows or videos, texting or chatting, playing games, or visiting social networking sites (Facebook, Twitter, Instagram). / Favor NO incluya el tiempo que pasa haciendo trabajos relacionados con la escuela, pero sí incluya el tiempo que pasa viendo televisión, programas o videos, enviando mensajes de texto o chateando, jugando videojuegos o visitando sitios de redes sociales (Facebook, Twitter, Instagram, etc.).

screentime_2_minutes_p:
On a typical WEEKEND DAY, how much TIME does your child spend on a computer, cellphone, tablet, or other electronic device?/ En un típico DIA DE FIN DE SEMANA, ¿cuánto TIEMPO pasa su niño(a) usando una computadora, un teléfono celular, una tableta u otro dispositivo electrónico? Minutes/ Minutos:
Please do NOT include time spent on school related work, but do include watching TV, shows or videos, texting or chatting, playing games, or visiting social networking sites (Facebook, Twitter, Instagram). / Favor NO incluya el tiempo que pasa haciendo trabajos relacionados con la escuela, pero sí incluya el tiempo que pasa viendo televisión, programas o videos, enviando mensajes de texto o chateando, jugando videojuegos o visitando sitios de redes sociales (Facebook, Twitter, Instagram, etc.).

## KSADS ADHD Composite
---------------------
DEAP name: None
Internal name: ksads_adhd_composite

Composite across the following ksads related ADHD variables ['ksads_14_853_p', 'ksads_14_854_p', 'ksads_14_855_p', 'ksads_14_856_p']


Binarized as if any questions answered yes, then treat as 1, otherwise 0.

Summed Questions:

ksads_14_853_p:
Diagnosis - Attention-Deficit/Hyperactivity Disorder Present

ksads_14_854_p:
Diagnosis - Attention-Deficit/Hyperactivity Disorder Past

ksads_14_855_p:
Diagnosis - Attention-Deficit/Hyperactivity Disorder IN PARTIAL REMISSION

ksads_14_856_p:
Diagnosis - Unspecified Attention-Deficit/Hyperactivity Disorder (F90.9)


## KSADS Bipolar Composite
---------------------
DEAP name: None
Internal name: ksads_bipolar_composite

Composite across the following ksads related bipolar variables 
['ksads_2_830_p', 'ksads_2_830_t', 'ksads_2_831_p',
 'ksads_2_831_t', 'ksads_2_832_p',
 'ksads_2_832_t', 'ksads_2_833_p',
 'ksads_2_833_t', 'ksads_2_834_p',
 'ksads_2_834_t', 'ksads_2_835_p',
 'ksads_2_835_t', 'ksads_2_836_p',
 'ksads_2_836_t', 'ksads_2_837_p',
 'ksads_2_837_t', 'ksads_2_838_p',
 'ksads_2_838_t', 'ksads_2_839_p',
 'ksads_2_839_t']

Summed Questions:

ksads_2_830_p:
Diagnosis - Bipolar I Disorder current episode manic (F31.1x)

ksads_2_830_t:
Diagnosis - Bipolar I Disorder, current episode manic (F31.1x)

ksads_2_831_p:
Diagnosis - Bipolar I Disorder current episode depressed F31.3x

ksads_2_831_t:
Diagnosis - Bipolar I Disorder, current episode depressed, F31.3x

ksads_2_832_p:
Diagnosis - Bipolar I Disorder currently hypomanic F31.0

ksads_2_832_t:
Diagnosis - Bipolar I Disorder, currently hypomanic F31.0

ksads_2_833_p:
Diagnosis - Bipolar I Disorder most recent past episode manic (F31.1x)

ksads_2_833_t:
Diagnosis - Bipolar I Disorder, most recent past episode manic (F31.1x)

ksads_2_834_p:
Diagnosis - Bipolar I Disorder most recent past episode depressed (F31.1.3x)

ksads_2_834_t:
Diagnosis - Bipolar I Disorder, most recent past episode depressed (F31.1.3x)

ksads_2_835_p:
Diagnosis - Bipolar II Disorder currently hypomanic ξF31.81

ksads_2_835_t:
Diagnosis - Bipolar II Disorder, currently hypomanic F31.81

ksads_2_836_p:
Diagnosis - Bipolar II Disorder currently depressed F31.81

ksads_2_836_t:
Diagnosis - Bipolar II Disorder, currently depressed F31.81

ksads_2_837_p:
Diagnosis - Bipolar II Disorder most recent past hypomanic ξF31.81

ksads_2_837_t:
Diagnosis - Bipolar II Disorder, most recent past hypomanic F31.81

ksads_2_838_p:
Diagnosis - Unspecified Bipolar and Related Disorder current ξ(F31.9)

ksads_2_838_t:
Diagnosis - Unspecified Bipolar and Related Disorder, current (F31.9)

ksads_2_839_p:
Diagnosis - Unspecified Bipolar and Related Disorder PAST (F31.9)

ksads_2_839_t:
Diagnosis - Unspecified Bipolar and Related Disorder, PAST (F31.9)


## KSADS OCD Composite
---------------------
DEAP name: None
Internal name: ksads_OCD_composite

Summed / composite measure of KSADS OCD related variables ['ksads_11_917_p', 'ksads_11_918_p', 'ksads_11_919_p', 'ksads_11_920_p']

Binarized as if any questions answered yes, then treat as 1, otherwise 0.

Summed Questions:

ksads_11_917_p:
Diagnosis - Obsessive-Compulsive Disorder Present (F42)

ksads_11_918_p:
Diagnosis - Obsessive-Compulsive Disorder Past (F42)

ksads_11_919_p:
Diagnosis - Other Specified Obsessive-Compulsive and Related Disorder present does not meet full criteria (F42)

ksads_11_920_p:
Diagnosis - Other Specified Obsessive-Compulsive and Related Disorder past does not meet full criteria (F42)

If any, set as 1, else 0.

## Sex at Birth
-----------------------------------
DEAP name: sex_at_birth

Sex at birth (takes value from NDA variable "sex")
F:Female | M: Male

## Sleep Disturbance Scale
--------------------
DEAP name: sleep_ss_total_p

Initial variable composed of total score (Sum of 6 Factors): sds_p_ss_dims + sds_p_ss_sbd + sds_p_ss_da + sds_p_ss_swtd + sds_p_ss_does + sds_p_ss_shy;
Validation: All items must be answered Bruni, O., Ottaviano, S., et al. (1996) The Sleep Disturbance Scale for Children (SDSC). Construction and validation of an instrument to evaluate sleep disturbances in childhood and adolescence. J Sleep Res 5(4): 251-261.

Summed Questions:

sds_p_ss_dims:
Disorders of Initiating and Maintaining Sleep (DIMS) SUM: sleepdisturb1_p + sleepdisturb2_p + sleepdisturb3_p + sleepdisturb4_p + sleepdisturb5_p + sleepdisturb10_p + sleepdisturb11_p; Validation: All items must be answered

sleep_ss_sbd:
search term: sds_p_ss_sbd
Sleep Breathing disorders (SBD): SUM sleepdisturb13_p + sleepdisturb14_p + sleepdisturb15_p; Validation: All items must be answered

sleep_ss_da:
Disorder of Arousal (DA) SUM: sleepdisturb17_p + sleepdisturb20_p + sleepdisturb21_p; Validation: All items must be answered

sleep_ss_swtd:
Sleep-Wake transition Disorders (SWTD) SUM: sleepdisturb6_p + sleepdisturb7_p + sleepdisturb8_p + sleepdisturb12_p + sleepdisturb18_p + sleepdisturb19_p; Validation: All items must be answered

sleep_ss_does:
Disorders of Excessive Somnolence (DOES) SUM: sleepdisturb22_p + sleepdisturb23_p + sleepdisturb24_p + sleepdisturb25_p + sleepdisturb26_p; Validation: All items must be answered

sleep_ss_shy:
Sleep Hyperhydrosis (SHY) SUM: sleepdisturb9_p + sleepdisturb16_p; Validation: All items must be answered

If greater than 35, set as 1, else <= 35, set as 0. 

## Detentions / Suspensions
-----------------------------
DEAP name: ksads_back_c_det_susp_p

In the past year, has you/your child had any detentions or suspensions? En el último año?/ ¿su niño(a) ha tenido alguna detención o suspensión en la escuela?
1 = Yes ; 2 = No ; 3 = Not sure; 777= Decline to answer

## Mental Health Services
--------------------------
DEAP name: ksads_back_c_mh_sa_p

Has your child ever received mental health or substance abuse services?/ ¿Su niño(a) ha recibido alguna vez servicios de salud mental o para el abuso de sustancias?

## Parents Married
-------------------
DEAP name: married.bl

Parents married? (baseline value carry forward)
0: No | 1: Yes

## Prodromal Psychosis Score
-------------------------------
DEAP name: prodrom_psych_ss_severity_score

Prodromal Psychosis: Severity Score Sum: (prodromal_1b_y, prodromal_2b_y, prodromal_3b_y, prodromal_4b_y, prodromal_5b_y, prodromal_6b_y, prodromal_7b_y, prodromal_8b_y, prodromal_9b_y, prodromal_10b_y, prodromal_11b_y, prodromal_12b_y, prodromal_13b_y, prodromal_14b_y, [prodromal_15b_y, prodromal_16b_y, prodromal_17b_y, prodromal_18b_y, prodromal_19b_y, prodromal_20b_y, prodromal_21b_y) + (pps_y_ss_ bother_n_1), If this score = "", then score = pps_y_ss_number; No minimum number of answers to be valid
Loewy, R. L., Pearson, R., et al. (2011) Psychosis risk screening with the Prodromal Questionnaire--brief version (PQ-B). Schizophr Res 129(1): 42-46. In the Prodromal Psychosis survey, "How much did it bother you?" is typically scored 2 - 6. In the version used by ABCD,  this item was scored  1 - 5. Because the "Did it bother you" sum score is equal to the sum of the number of severity scores used in the severity score calculation, we were able to compensate for this scoring difference by adding the "Did it bother you" sum score to the severity score.  After applying this change, the severity scores reported here are comparable to those calculated using the  "How much did it bother you"  2 - 6  scoring range.

Used Questions:

prodromal_1b_y:
Well known places. Please CHOOSE THE NUMBER below the appropriate picture that shows us how much that bothered you when it happened.
1 = 1; 2 = 2; 3 = 3; 4 = 4; 5 = 5

prodromal_2b_y:
Strange sounds. Please CHOOSE THE NUMBER below the appropriate picture that shows us how much that bothered you when it happened.
1 = 1; 2 = 2; 3 = 3; 4 = 4; 5 = 5

prodromal_3b_y:
Things looked different.Please CHOOSE THE NUMBER below the appropriate picture that shows us how much that bothered you when it happened.
1 = 1; 2 = 2; 3 = 3; 4 = 4; 5 = 5

prodromal_4b_y:
Special powers. Please CHOOSE THE NUMBER below the appropriate picture that shows us how much that bothered you when it happened.
1 = 1; 2 = 2; 3 = 3; 4 = 4; 5 = 5

prodromal_5b_y:
Someone else in control. Please CHOOSE THE NUMBER below the appropriate picture that shows us how much that bothered you when it happened.
1 = 1; 2 = 2; 3 = 3; 4 = 4; 5 = 5

prodromal_6b_y:
Hard to figure out. Please CHOOSE THE NUMBER below the appropriate picture that shows us how much that bothered you when it happened.
1 = 1; 2 = 2; 3 = 3; 4 = 4; 5 = 5

prodromal_7b_y:
Magical talents. Please CHOOSE THE NUMBER below the appropriate picture that shows us how much that bothered you when it happened.
1 = 1; 2 = 2; 3 = 3; 4 = 4; 5 = 5

prodromal_8b_y:
Could not trust. Please CHOOSE THE NUMBER below the appropriate picture that shows us how much that bothered you when it happened.
1 = 1; 2 = 2; 3 = 3; 4 = 4; 5 = 5

prodromal_9b_y:
Strange skin feelings. Please CHOOSE THE NUMBER below the appropriate picture that shows us how much that bothered you when it happened.
1 = 1; 2 = 2; 3 = 3; 4 = 4; 5 = 5

prodromal_10b_y:
Lose concentration. Please CHOOSE THE NUMBER below the appropriate picture that shows us how much that bothered you when it happened.
1 = 1; 2 = 2; 3 = 3; 4 = 4; 5 = 5

prodromal_11b_y:
Invisible energy. Please CHOOSE THE NUMBER below the appropriate picture that shows us how much that bothered you when it happened.
1 = 1; 2 = 2; 3 = 3; 4 = 4; 5 = 5

prodromal_12b_y:
Mind is trying to trick you. Please CHOOSE THE NUMBER below the appropriate picture that shows us how much that bothered you when it happened.
1 = 1; 2 = 2; 3 = 3; 4 = 4; 5 = 5

prodromal_13b_y:
World is not real. Please CHOOSE THE NUMBER below the appropriate picture that shows us how much that bothered you when it happened.
1 = 1; 2 = 2; 3 = 3; 4 = 4; 5 = 5

prodromal_14b_y:
Feel confused. Please CHOOSE THE NUMBER below the appropriate picture that shows us how much that bothered you when it happened.
1 = 1; 2 = 2; 3 = 3; 4 = 4; 5 = 5

prodromal_15b_y:
Did you honestly believe in things that other people would say are unusual or weird. Please CHOOSE THE NUMBER below the appropriate picture that shows us how much that bothered you when it happened.
1 = 1; 2 = 2; 3 = 3; 4 = 4; 5 = 5

prodromal_16b_y:
Body changed. Please CHOOSE THE NUMBER below the appropriate picture that shows us how much that bothered you when it happened.
1 = 1; 2 = 2; 3 = 3; 4 = 4; 5 = 5

prodromal_17b_y:
Hear thoughts. Please CHOOSE THE NUMBER below the appropriate picture that shows us how much that bothered you when it happened.
1 = 1; 2 = 2; 3 = 3; 4 = 4; 5 = 5

prodromal_18b_y:
People want bad things to happen.Please CHOOSE THE NUMBER below the appropriate picture that shows us how much that bothered you when it happened.
1 = 1; 2 = 2; 3 = 3; 4 = 4; 5 = 5

prodromal_19b_y:
Unusual things. Please CHOOSE THE NUMBER below the appropriate picture that shows us how much that bothered you when it happened.
1 = 1; 2 = 2; 3 = 3; 4 = 4; 5 = 5

prodromal_20b_y:
Able to see more than others. Please CHOOSE THE NUMBER below the appropriate picture that shows us how much that bothered you when it happened.
1 = 1; 2 = 2; 3 = 3; 4 = 4; 5 = 5

prodromal_21b_y:
Hard time understanding you. Please CHOOSE THE NUMBER below the appropriate picture that shows us how much that bothered you when it happened.
1 = 1; 2 = 2; 3 = 3; 4 = 4; 5 = 5

pps_y_ss_bother_n_1:
Prodromal Psychosis Scale: Number of No Responses to Did it Bother You? Intermediate equation for Severity Score Sum: pps_1_bother_yn, pps_2_bother_yn, pps_3_bother_yn, pps_4_bother_yn, pps_5_bother_yn, pps_6_bother_yn, pps_7_bother_yn, pps_8_bother_yn, pps_9_bother_yn, pps_10_bother_yn, pps_11_bother_yn, pps_12_bother_yn, pps_13_bother_yn, pps_14_bother_yn, pps_15_bother_yn, pps_16_bother_yn, pps_17_bother_yn, pps_18_bother_yn, pps_19_bother_yn, pps_20_bother_yn, pps_21_bother_yn; No minimum number of answers to be valid