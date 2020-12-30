# -*- coding: utf-8 -*-

"""American vs. British"""

from proselint.tools import memoize, preferred_forms_check


@memoize
def check(text):
    """American vs. British"""
    err = "spelling_usa.main"
    msg = "American vs. British '{}' is the preferred spelling."

    preferences = [
        ["adaptor", ["adapter"]],
        ["adrenaline", ["adrenalin"]],
        ["aeroplane", ["airplane"]],
        ["aluminium", ["aluminum"]],
        ["analogue", ["analog"]],
        ["analyse", ["analyze"]],
        ["analysed", ["analyzed"]],
        ["analyser", ["analyzer"]],
        ["analysing", ["analyzing"]],
        ["anaemia", ["anemia"]],
        ["anaesthesia", ["anesthesia"]],
        ["anaesthetist", ["anesthesiologist"]],
        ["anaesthetic", ["anesthetic"]],
        ["antennae", ["antennas"]],
        ["anti-aliased", ["antialiased"]],
        ["anti-aliasing", ["antialiasing"]],
        ["any more", ["anymore"]],
        ["appal", ["appall"]],
        ["archaeology", ["archeology"]],
        ["armour", ["armor"]],
        ["artefact", ["artifact"]],
        ["authorisation", ["authorization"]],
        ["authorisational", ["authorizational"]],
        ["authorise", ["authorize"]],
        ["authorised", ["authorized"]],
        ["authorising", ["authorizing"]],
        ["axe", ["ax"]],
        ["baulk", ["balk"]],
        ["farmyard", ["barnyard"]],
        ["basically", ["basicly"]],
        ["beetroot", ["beet"]],
        ["behaviour", ["behavior"]],
        ["behove", ["behoove"]],
        ["bulldog clip", ["binder clip"]],
        ["bobsleigh", ["bobsled"]],
        ["bogey", ["boogey"]],
        ["broke", ["braked"]],
        ["grill", ["broil"]],
        ["burnt", ["burned"]],
        ["café", ["cafe"]],
        ["calibre", ["caliber"]],
        ["cancelled", ["canceled"]],
        ["cancelling", ["canceling"]],
        ["capitalisation", ["capitalization"]],
        ["capitalise", ["capitalize"]],
        ["capitalised", ["capitalized"]],
        ["capitalising", ["capitalizing"]],
        ["carburettor", ["carburetor"]],
        ["case-insensitive", ["case insensitive"]],
        ["case-sensitive", ["case sensitive"]],
        ["castor", ["caster"]],
        ["catalogue", ["catalog"]],
        ["categorisation", ["categorization"]],
        ["categorise", ["categorize"]],
        ["categorised", ["categorized"]],
        ["categorising", ["categorizing"]],
        ["centimetre", ["centimeter"]],
        ["centre", ["center"]],
        ["centred", ["centered"]],
        ["centring", ["centering"]],
        ["centralisation", ["centralization"]],
        ["centralise", ["centralize"]],
        ["centralised", ["centralized"]],
        ["centralising", ["centralizing"]],
        ["caesium", ["cesium"]],
        ["tickbox", ["checkbox"]],
        ["chequer", ["checker"]],
        ["chequerboard", ["checkerboard"]],
        ["chequered", ["checkered"]],
        ["cypher", ["cipher"]],
        ["café", ["coffee shop"]],
        ["colour", ["color"]],
        ["coloured", ["colored"]],
        ["colourer", ["colorer"]],
        ["colourful", ["colorful"]],
        ["colouring", ["coloring"]],
        ["colour-key", ["colorkey"]],
        ["colour-space", ["colorspace"]],
        ["co-operate", ["cooperate"]],
        ["co-ordinate", ["coordinate"]],
        ["candy floss", ["cotton candy"]],
        ["anti-clockwise", ["counterclockwise"]],
        ["anti-clockwise", ["counter-clockwise"]],
        ["coupé", ["coupe"]],
        ["overalls", ["coveralls"]],
        ["cosy", ["cozy"]],
        ["curricula", ["curriculums"]],
        ["customisable", ["customizable"]],
        ["customisation", ["customization"]],
        ["customise", ["customize"]],
        ["customised", ["customized"]],
        ["customising", ["customizing"]],
        ["dealt", ["dealed"]],
        ["defence", ["defense"]],
        ["dialled", ["dialed"]],
        ["dialler", ["dialer"]],
        ["dialling", ["dialing"]],
        ["dialogue", ["dialog"]],
        ["diarrhoea", ["diarrhea"]],
        ["digitisation", ["digitization"]],
        ["digitise", ["digitize"]],
        ["digitised", ["digitized"]],
        ["digitiser", ["digitizer"]],
        ["digitising", ["digitizing"]],
        ["dish cloth", ["dishrag"]],
        ["tea towel", ["dishtowel"]],
        ["disorganised", ["disorganized"]],
        ["distil", ["distill"]],
        ["doughnut", ["donut"]],
        ["drainpipe", ["downspout"]],
        ["draught", ["draft"]],
        ["dreamt", ["dreamed"]],
        ["pharmacy", ["drugstore"]],
        ["skip", ["dumpster"]],
        ["encyclopaedia", ["encyclopedia"]],
        ["endeavour", ["endeavor"]],
        ["oenology", ["enology"]],
        ["equalled", ["equaled"]],
        ["equalling", ["equaling"]],
        ["equalise", ["equalize"]],
        ["equalised", ["equalized"]],
        ["equaliser", ["equalizer"]],
        ["equalising", ["equalizing"]],
        ["oesophagus", ["esophagus"]],
        ["aesthetics", ["esthetics"]],
        ["familiarisation", ["familiarization"]],
        ["familiarise", ["familiarize"]],
        ["familiarised", ["familiarized"]],
        ["familiarising", ["familiarizing"]],
        ["bum bag", ["fanny pack"]],
        ["tap", ["faucet"]],
        ["favour", ["favor"]],
        ["favoured", ["favored"]],
        ["favouring", ["favoring"]],
        ["favourite", ["favorite"]],
        ["foetus", ["fetus"]],
        ["fibre", ["fiber"]],
        ["fillet", ["filet"]],
        ["fill in", ["fill out"]],
        ["orch", ["flashlight"]],
        ["cutlery", ["flatware"]],
        ["flavour", ["flavor"]],
        ["flavoured", ["flavored"]],
        ["flavouring", ["flavoring"]],
        ["formulae", ["formulas"]],
        ["quarter", ["fourth"]],
        ["hot chips", ["french fries"]],
        ["fuelled", ["fueled"]],
        ["fuelling", ["fueling"]],
        ["furore", ["furor"]],
        ["rubbish", ["garbage"]],
        ["petrol", ["gasoline"]],
        ["globalisation", ["globalization"]],
        ["globalisational", ["globalizational"]],
        ["globalise", ["globalize"]],
        ["globalised", ["globalized"]],
        ["globalising", ["globalizing"]],
        ["globally", ["globaly"]],
        ["glycerine", ["glycerin"]],
        ["goitre", ["goiter"]],
        ["grey", ["gray"]],
        ["greylist", ["graylist"]],
        ["greylisted", ["graylisted"]],
        ["greylisting", ["graylisting"]],
        ["guerrilla", ["guerilla"]],
        ["gynaecology", ["gynecology"]],
        ["harbour", ["harbor"]],
        ["harboured", ["harbored"]],
        ["harbouring", ["harboring"]],
        ["haemophilia", ["hemophilia"]],
        ["haemophiliac", ["hemophiliac"]],
        ["haulier", ["hauler"]],
        ["homoeopathic", ["homeopathic"]],
        ["homoeopathy", ["homeopathy"]],
        ["honour", ["honor"]],
        ["honoured", ["honored"]],
        ["honouring", ["honoring"]],
        ["humour", ["humor"]],
        ["humoured", ["humored"]],
        ["humouring", ["humoring"]],
        ["unfeasible", ["infeasible"]],
        ["initialisation", ["initialization"]],
        ["initialisational", ["initializational"]],
        ["initialise", ["initialize"]],
        ["initialised", ["initialized"]],
        ["initialiser", ["initializer"]],
        ["initialising", ["initializing"]],
        ["internationalisation", ["internationalization"]],
        ["internationalisational", ["internationalizational"]],
        ["internationalise", ["internationalize"]],
        ["internationalised", ["internationalized"]],
        ["internationalising", ["internationalizing"]],
        ["jelly", ["jello"]],
        ["jelly", ["jell-o"]],
        ["jewelled", ["jeweled"]],
        ["jeweller", ["jeweler"]],
        ["jewellery", ["jewelery"]],
        ["journalling", ["journaling"]],
        ["judgement", ["judgment"]],
        ["kilometre", ["kilometer"]],
        ["knelt", ["kneeled"]],
        ["labelled", ["labeled"]],
        ["labeller", ["labeler"]],
        ["labelling", ["labeling"]],
        ["labour", ["labor"]],
        ["laboured", ["labored"]],
        ["labouring", ["laboring"]],
        ["ladybird", ["ladybug"]],
        ["surname", ["last name"]],
        ["leant", ["leaned"]],
        ["lept", ["leaped"]],
        ["learnt", ["learned"]],
        ["leukaemia", ["leukemia"]],
        ["number plate", ["license plate"]],
        ["liquorice", ["licorice"]],
        ["lit", ["lighted"]],
        ["litre", ["liter"]],
        ["localisation", ["localization"]],
        ["localisational", ["localizational"]],
        ["localise", ["localize"]],
        ["localised", ["localized"]],
        ["localising", ["localizing"]],
        ["letterbox", ["mailbox"]],
        ["postman", ["mailman"]],
        ["letterbox", ["mail slot"]],
        ["maths", ["math"]],
        ["mediaeval", ["medieval"]],
        ["millilitre", ["milliliter"]],
        ["millimetre", ["millimeter"]],
        ["minimise", ["minimize"]],
        ["minimised", ["minimized"]],
        ["minimising", ["minimizing"]],
        ["misspelt", ["misspelled"]],
        ["modelled", ["modeled"]],
        ["modeller", ["modeler"]],
        ["modelling", ["modeling"]],
        ["mould", ["mold"]],
        ["moult", ["molt"]],
        ["mum", ["mom"]],
        ["mumma", ["momma"]],
        ["mummy", ["mommy"]],
        ["mum-and-dad", ["mom-and-pop"]],
        ["film", ["movie"]],
        ["moustache", ["mustache"]],
        ["nanometre", ["nanometer"]],
        ["neighbour", ["neighbor"]],
        ["neighbouring", ["neighboring"]],
        ["neurone", ["neuron"]],
        ["newsagent", ["newsdealer"]],
        ["normality", ["normalcy"]],
        ["normalisation", ["normalization"]],
        ["normalise", ["normalize"]],
        ["normalised", ["normalized"]],
        ["normalising", ["normalizing"]],
        ["offence", ["offense"]],
        ["off", ["off of"]],
        ["often", ["oftentimes"]],
        ["optimisation", ["optimization"]],
        ["optimisational", ["optimizational"]],
        ["optimise", ["optimize"]],
        ["optimised", ["optimized"]],
        ["optimising", ["optimizing"]],
        ["organisation", ["organization"]],
        ["organisational", ["organizational"]],
        ["organise", ["organize"]],
        ["organised", ["organized"]],
        ["organiser", ["organizer"]],
        ["organising", ["organizing"]],
        ["irritable", ["ornery"]],
        ["orthopaedic", ["orthopedic"]],
        ["ousting", ["ouster"]],
        ["dummy", ["pacifier"]],
        ["pyjamas", ["pajamas"]],
        ["panelled", ["paneled"]],
        ["panelling", ["paneling"]],
        ["tights", ["pantyhose"]],
        ["bracket", ["paren"]],
        ["brackets", ["parentheses"]],
        ["bracket", ["parenthesis"]],
        ["bracketed", ["parenthesized"]],
        ["car park", ["parking lot"]],
        ["paediatric", ["pediatric"]],
        ["pernickety", ["persnickety"]],
        ["picometre", ["picometer"]],
        ["plough", ["plow"]],
        ["suffix", ["postpend"]],
        ["première", ["premiere"]],
        ["prefix", ["prepend"]],
        ["prioritisation", ["prioritization"]],
        ["prioritise", ["prioritize"]],
        ["prioritised", ["prioritized"]],
        ["prioritising", ["prioritizing"]],
        ["pin", ["prong"]],
        ["quin", ["quint"]],
        ["railway", ["railroad"]],
        ["randomisation", ["randomization"]],
        ["randomise", ["randomize"]],
        ["randomised", ["randomized"]],
        ["randomising", ["randomizing"]],
        ["abseil", ["rappel"]],
        ["real estate agent", ["realator"]],
        ["realisation", ["realization"]],
        ["realise", ["realize"]],
        ["realised", ["realized"]],
        ["realising", ["realizing"]],
        ["recognisable", ["recognizable"]],
        ["recognise", ["recognize"]],
        ["recognised", ["recognized"]],
        ["ecognising", ["recognizing"]],
        ["reinitialise", ["reinitialize"]],
        ["reinitialised", ["reinitialized"]],
        ["reinitialising", ["reinitializing"]],
        ["terraced house", ["row house"]],
        ["rumour", ["rumor"]],
        ["rumoured", ["rumored"]],
        ["sabre", ["saber"]],
        ["sailing boat", ["sailboat"]],
        ["sanatorium", ["sanitarium"]],
        ["scallywag", ["scalawag"]],
        ["sceptre", ["scepter"]],
        ["serialisation", ["serialization"]],
        ["serialisational", ["serializational"]],
        ["serialise", ["serialize"]],
        ["serialised", ["serialized"]],
        ["serialising", ["serializing"]],
        ["charivari", ["shivaree"]],
        ["pavement", ["sidewalk"]],
        ["signalled", ["signaled"]],
        ["signalling", ["signaling"]],
        ["simultaneous", ["simultanous"]],
        ["sceptic", ["skeptic"]],
        ["sceptical", ["skeptical"]],
        ["scepticism", ["skepticism"]],
        ["sleigh", ["sled"]],
        ["specialisation", ["specialization"]],
        ["specialisational", ["specializational"]],
        ["specialise", ["specialize"]],
        ["specialised", ["specialized"]],
        ["specialising", ["specializing"]],
        ["speciality", ["specialty"]],
        ["spectre", ["specter"]],
        ["spelt", ["spelled"]],
        ["spilt", ["spilled"]],
        ["spiralled", ["spiraled"]],
        ["spiralling", ["spiraling"]],
        ["spoilt", ["spoiled"]],
        ["standardise", ["standardize"]],
        ["gear stick", ["stickshift"]],
        ["tram", ["streetcar"]],
        ["pram", ["stroller"]],
        ["sulphur", ["sulfur"]],
        ["sulphurous", ["sulfurous"]],
        ["summarisation", ["summarization"]],
        ["summarisational", ["summarizational"]],
        ["summarise", ["summarize"]],
        ["summarised", ["summarized"]],
        ["summarising", ["summarizing"]],
        ["symbolisation", ["symbolization"]],
        ["symbolisational", ["symbolizational"]],
        ["symbolise", ["symbolize"]],
        ["symbolised", ["symbolized"]],
        ["symbolising", ["symbolizing"]],
        ["synchronisation", ["synchronization"]],
        ["synchronisational", ["synchronizational"]],
        ["synchronise", ["synchronize"]],
        ["synchronised", ["synchronized"]],
        ["synchronising", ["synchronizing"]],
        ["synthesise", ["synthesize"]],
        ["toffee", ["taffy"]],
        ["exhaust pipe", ["tailpipe"]],
        ["templatisation", ["templatization"]],
        ["templatisational", ["templatizational"]],
        ["templatise", ["templatize"]],
        ["templatised", ["templatized"]],
        ["templatising", ["templatizing"]],
        ["theatre", ["theater"]],
        ["drawing pin", ["thumbtack"]],
        ["titbit", ["tidbit"]],
        ["totalled", ["totaled"]],
        ["totaller", ["totaler"]],
        ["totalling", ["totaling"]],
        ["trolleybus", ["trackless trolley"]],
        ["transport", ["transportation"]],
        ["uncategorised", ["uncategorized"]],
        ["unauthorised", ["unauthorized"]],
        ["uninitialisation", ["uninitialization"]],
        ["uninitialisational", ["uninitializational"]],
        ["uninitialise", ["uninitialize"]],
        ["uninitialised", ["uninitialized"]],
        ["uninitialising", ["uninitializing"]],
        ["unorganised", ["unorganized"]],
        ["unrecognisable", ["unrecognizable"]],
        ["unrecognised", ["unrecognized"]],
        ["forthcoming", ["upcoming"]],
        ["upmarket", ["upscale"]],
        ["usable", ["useable"]],
        ["utilisation", ["utilization"]],
        ["utilise", ["utilize"]],
        ["utilised", ["utilized"]],
        ["utilising", ["utilizing"]],
        ["vapour", ["vapor"]],
        ["vectorization", ["vectorisation"]],
        ["vectorisational", ["vectorizational"]],
        ["vectorise", ["vectorize"]],
        ["vectorised", ["vectorized"]],
        ["vectoriser", ["vectorizer"]],
        ["vectorising", ["vectorizing"]],
        ["virtualisation", ["virtualization"]],
        ["virtualise", ["virtualize"]],
        ["virtualised", ["virtualized"]],
        ["virtualising", ["virtualizing"]],
        ["vice", ["vise"]],
        ["visualisation", ["visualization"]],
        ["visualise", ["visualize"]],
        ["visualised", ["visualized"]],
        ["visualising", ["visualizing"]],
        ["windscreen", ["windshield"]],
        ["yoghurt", ["yogurt"]],
    ]

    return preferred_forms_check(text, preferences, err, msg)
