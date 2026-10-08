# What is Rendering?

*Dictionary · Dev · Last updated: September 22, 2026*

Rendering is the process of converting raw data into the image you see on the screen.

## Definition and Word Origin

"Render" means to present or draw in English. Computers keep data in numbers. Rendering converts this digital data into an image that you can see by calculating the light, color and shape properties. This process requires intense mathematical calculations, so the graphics card (GPU) usually takes care of it.

***Analogy:** It is like a chef using the raw ingredients (data) he has and transforming them into a plate (visual) ready for presentation.*

## How to Know and Use in Daily Life?

**Web pages:** Your browser draws the HTML and CSS code on the screen, pixel by pixel.
**Games:** Generating new frames 30 or 60 times per second.
**Video editing:** Conversion (export) of the effects timeline into watchable video.
**Maps:** Drawing new details as you zoom in.

## Technical Depth and Architecture

There are two main ways to create images:

**Rasterization:** The three-dimensional scene is divided into triangles, each triangle is converted into pixels. It's fast, standard in games.
**Ray tracing:** The path of light beams on the stage is followed in reverse. Reflection and shadows become realistic, but much more expensive.

Two approaches are also discussed on the web side:

**Rendering on server (SSR):** The page is drawn on the server and ready HTML is sent. The first boot is fast.
**Render on client (CSR):** A blank page comes up, the content is drawn with JavaScript in the browser. Afterwards it is smooth, the first opening is slow.

Frame rate (FPS) determines the experience: As the value decreases, you will feel stuttering. Slowness is usually caused by the amount of data to be processed exceeding the hardware.

## Use in Different Disciplines

**Printing press:** Converting the page design into a printing plate.
**Architectural:** A realistic three-dimensional visual (situation) of the project.
**Cinema:** Frame calculation of post-shooting effects.

## Frequently Asked Questions

**Why might rendering be slow?**

If the amount of data to be processed exceeds the capacity of the hardware, the process slows down. The solution is usually to cut back on detail, reinforce equipment, or break the job into parts.

**What is ray tracing?**

It is a method that realistically calculates reflections and shadows by following the path of light beams in the scene. It is of high quality, but requires much more processing power than rasterization.

**What is the difference between SSR and CSR?**

SSR draws the page on the server and sends it ready, making the first opening faster. CSR leaves the drawing to the browser, the first opening is slow, but afterwards it is smooth.

**Is a powerful graphics card necessary for rendering?**

Not always. The processor is sufficient for web pages and office work. Gaming, 3D design and video works require a powerful graphics card.

## Related terms

- [GUI](https://trescout.com/en/dictionary/gui/)
- [User Interface](https://trescout.com/en/dictionary/user-interface/)
- [Frontend Stack](https://trescout.com/en/dictionary/frontend-stack/)

## Related tools

- [Next.js](https://trescout.com/en/discover/next-js/)
- [Nuxt](https://trescout.com/en/discover/nuxt/)
- [Meshoptimizer](https://trescout.com/en/discover/meshoptimizer/)

This explanation was written in plain language for TreScout and **machine-translated** from the Turkish original · the Turkish version prevails. If something looks wrong or missing, write to [hello@trescout.com](mailto:hello@trescout.com). [Read in Turkish →](https://trescout.com/dictionary/rendering/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/rendering/
