import BasicAPI from "@/network/basicAPI.js";

const ImgAPI = new BasicAPI()

export async function getStyles() {
    const response =  await ImgAPI({
        method: 'GET',
        url: '/getStyle'
    })
    console.log(response)
    return response
}

export async function Generate(prompt, negative_prompt = "",
                               styles = "", seed = 516516,
                               scale = 5, sampler = "DDIM",
                               steps = 50) {
    const payload = {
        prompt: prompt,
        negative_prompt: negative_prompt,
        styles: styles,
        seed: seed,
        scale: scale,
        sampler: sampler,
        steps: steps
    }
    return await ImgAPI.post('/getSDXL', payload)
}
