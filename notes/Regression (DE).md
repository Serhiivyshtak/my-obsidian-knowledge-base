# Regression

In vielen Situationen des Alltags und der Wissenschaft möchten wir **Zahlen vorhersagen** — etwa wie viele Produkte morgen verkauft werden, wie hoch die Temperatur nächste Woche sein wird oder wie lange eine Maschine noch funktionieren wird. Die Methode, mit der solche Vorhersagen systematisch getroffen werden, nennt man **Regression**. Diese Zusammenfassung erklärt das Konzept anhand anschaulicher Beispiele und grenzt es von verwandten Methoden ab.

## Was ist Regression?

> **Definition:** Regression bezeichnet die Vorhersage einer *messbaren Größe* mithilfe von Werten, die mit dieser Größe in Zusammenhang stehen.

Um diese Definition besser zu verstehen, ist es wichtig zu klären, was genau eine **messbare Größe** ist. Nicht jede Zahl, die uns begegnet, eignet sich für Regression.

### Was macht eine Größe "messbar"?

Eine Größe gilt als messbar, wenn sie bestimmte Eigenschaften erfüllt. Erstens müssen die Zahlenwerte eine **sinnvolle Ordnung** beschreiben. Wenn wir sagen *"100 Portionen sind weniger als 200 Portionen"*, dann ergibt das Sinn — 100 ist tatsächlich kleiner als 200, und dieser Unterschied hat eine praktische Bedeutung.

Zweitens sollten **Nachkommastellen sinnvoll** sein. Es ist völlig vernünftig zu sagen: *"Im Schnitt werden 223,7 Portionen Eis pro Tag verkauft."* Auch wenn man keine 0,7 Portionen tatsächlich verkaufen kann, ist der Durchschnittswert als statistische Größe aussagekräftig.

Drittens sollten die Werte **gerundet oder gemittelt** werden können, ohne ihre Bedeutung zu verlieren. Wenn wir die Verkaufszahlen einer Woche zusammenfassen oder den Durchschnitt bilden, erhalten wir weiterhin nützliche Informationen.

### Beispiel: Eisverkäufe vorhersagen

Ein klassisches Beispiel für Regression ist die Vorhersage von **Eisverkäufen**. Die Anzahl der verkauften Portionen an einem Tag ist eine messbare Größe — sie hat eine sinnvolle Ordnung, kann Nachkommastellen haben (als Durchschnitt) und lässt sich problemlos mitteln.

Die Vorhersage wird besser, wenn wir **Faktoren berücksichtigen**, die mit den Verkaufszahlen zusammenhängen. Bei Eisverkäufen sind das beispielsweise die **Bewölkung**, die **Temperatur** und die **Lage** des Verkaufsstands. Diese Faktoren helfen uns, genauere Vorhersagen zu treffen.

### Weitere Anwendungsbeispiele

Regression findet in zahlreichen Bereichen Anwendung:

| Anwendung | Vorherzusagende Größe | Mögliche Einflussfaktoren |
|-----------|----------------------|---------------------------|
| Wettervorhersage | Höchsttemperaturen, Niederschlagsmengen | Jahreszeit, Luftdruck, Windrichtung |
| Wartungsplanung | Verbleibende Lebensdauer von Verschleißteilen | Betriebsstunden, Belastung, Alter |
| Finanzwesen | Preisentwicklungen, Aktienkurse | Marktdaten, Wirtschaftsindikatoren |
| Logistik | Wartezeiten | Tageszeit, Auslastung, Personal |
| Biometrie | Schuhgröße | Körpergröße, biologisches Geschlecht, Alter |

Bei der Vorhersage der Schuhgröße etwa helfen Faktoren wie Körpergröße, biologisches Geschlecht und Alter. Allerdings ist es wichtig zu beachten, dass Vorhersagen **praktisch nie perfekt** sind — es gibt immer individuelle Abweichungen und unbekannte Einflussfaktoren.

---

## Was ist keine Regression?

Um das Konzept der Regression besser zu verstehen, hilft es, sich anzuschauen, welche Vorhersageprobleme **nicht** zur Regression gehören. Diese fallen stattdessen in den Bereich der **Klassifikation**.

> **Abgrenzung:** Klassifikation ist die Vorhersage, welcher Wert aus einer *begrenzten Menge* von Werten der richtige ist.

### Beispiele für Klassifikation (keine Regression)

**Lieblingsessen vorhersagen:** Das Ergebnis ist keine Zahl, sondern ein Element aus einer Liste möglicher Gerichte. Es gibt keine sinnvolle Ordnung — *"Pizza"* ist nicht mehr oder weniger als *"Pasta"*.

**Ergebnis eines Münzwurfs vorhersagen:** Obwohl man Kopf und Zahl theoretisch als 0 und 1 kodieren könnte, beschreibt diese Zahl keine messbare Größe. Es gibt keine sinnvolle Ordnung, und Zwischenwerte wie 0,5 haben keine Bedeutung für einen einzelnen Wurf.

**Telefonnummern vorhersagen:** Telefonnummern sind zwar Zahlen, aber sie beschreiben keine messbare Größe. Die Nummer *0711* ist nicht kleiner als *07121* in irgendeinem sinnvollen Sinne. Telefonnummern haben keine Nachkommastellen, und der Durchschnitt zweier Telefonnummern ergibt keinen Sinn.

---

## Wann funktioniert Regression?

Die entscheidende Frage bei jeder Regression ist: **Welche Faktoren helfen bei der Vorhersage?** Hier unterscheidet man zwischen zwei Arten von Zusammenhängen.

### Prädiktive Faktoren

> **Definition:** Ein *prädiktiver Faktor* ist ein Faktor, der mit der vorherzusagenden Größe irgendwie in Zusammenhang steht und daher bei der Vorhersage hilfreich ist.

Das Wort *prädiktiv* bedeutet so viel wie "vorhersagend" oder "hinweisend". Bei der Vorhersage von Eisverkäufen ist das **Wetter** ein prädiktiver Faktor, weil es einen Zusammenhang gibt zwischen dem Wetter und der Lust auf Eis. Wenn wir das Wetter kennen, können wir bessere Vorhersagen über die Verkaufszahlen treffen.

Das Entscheidende ist: Bei der Regression können **beliebige Faktoren** hilfreich sein, solange sie irgendwie mit der vorherzusagenden Größe zusammenhängen. Der Zusammenhang muss dabei nicht einmal ursächlich sein — es reicht, wenn er statistisch besteht.

### Kausale Faktoren

> **Definition:** Ein *kausaler Faktor* ist ein Faktor, der die vorherzusagende Größe direkt *verursacht* oder beeinflusst.

Bei den Eisverkäufen ist die **Temperatur** ein kausaler Faktor. An heißen Tagen wird mehr Eis verkauft, *weil* es heiß ist. Die Hitze ist die direkte Ursache für den erhöhten Eiskonsum — Menschen haben bei Wärme mehr Lust auf eine kühle Erfrischung.

Kausale Faktoren sind immer auch prädiktiv, aber nicht jeder prädiktive Faktor ist kausal.

### Der Unterschied zwischen Korrelation und Kausalität

Ein besonders lehrreiches Beispiel verdeutlicht den Unterschied zwischen prädiktiven und kausalen Zusammenhängen. Betrachten wir den Zusammenhang zwischen der **Anzahl privater Swimming Pools** in einem Stadtteil und den dortigen **Absatzzahlen für Champagner**.

Tatsächlich gibt es einen statistischen Zusammenhang: In Stadtteilen mit vielen Pools wird auch viel Champagner verkauft. Beide Faktoren sind daher gegenseitig **prädiktiv** — wenn wir die Anzahl der Pools kennen, können wir die Champagner-Verkäufe besser vorhersagen, und umgekehrt.

Aber dieser Zusammenhang ist **nicht kausal**. Es wird nicht mehr Champagner verkauft, *weil* es besonders viele Pools gibt. Und es werden auch nicht mehr Pools gebaut, *weil* viel Champagner gekauft wurde. Stattdessen gibt es einen **gemeinsamen kausalen Faktor**: das Vermögen der Bevölkerung. Wohlhabende Menschen können sich sowohl Pools als auch Champagner leisten — das Vermögen beeinflusst beide Größen kausal.

Für die Regression ist diese Unterscheidung oft nicht entscheidend: Solange ein Zusammenhang besteht, kann er für Vorhersagen genutzt werden. Für das **Verständnis** der Zusammenhänge und für **Interventionen** (also wenn wir etwas verändern wollen) ist die Unterscheidung zwischen Korrelation und Kausalität jedoch fundamental wichtig.

---

## Zusammenfassung der wichtigsten Konzepte

| Begriff | Bedeutung |
|---------|-----------|
| **Regression** | Vorhersage einer messbaren Größe basierend auf zusammenhängenden Faktoren |
| **Messbare Größe** | Eine Zahl mit sinnvoller Ordnung, möglichen Nachkommastellen und der Fähigkeit, gemittelt zu werden |
| **Klassifikation** | Vorhersage einer Kategorie aus einer begrenzten Menge (Abgrenzung zur Regression) |
| **Prädiktiver Faktor** | Ein Faktor, der mit der Zielgröße zusammenhängt und bei der Vorhersage hilft |
| **Kausaler Faktor** | Ein Faktor, der die Zielgröße direkt verursacht oder beeinflusst |
| **Korrelation** | Statistischer Zusammenhang zwischen zwei Größen (nicht notwendigerweise ursächlich) |

## Fazit

Regression ist ein mächtiges Werkzeug zur Vorhersage von Zahlen, aber ihr Erfolg hängt entscheidend davon ab, **prädiktive Faktoren** zu identifizieren. Diese müssen nicht kausal sein — jeder Zusammenhang, der statistisch besteht, kann für bessere Vorhersagen genutzt werden. Gleichzeitig ist es wichtig, die Grenzen der Regression zu kennen: Sie eignet sich nur für messbare Größen und liefert niemals perfekte Vorhersagen. Das Verständnis des Unterschieds zwischen Korrelation und Kausalität schützt vor Fehlinterpretationen und hilft, die Ergebnisse richtig einzuordnen.

---

*Quelle: "Regression" von Dr. Antje Schweitzer, Universität Stuttgart, Institut für Maschinelle Sprachverarbeitung / Institut für Software Engineering. Lizenziert unter CC BY 4.0.*
