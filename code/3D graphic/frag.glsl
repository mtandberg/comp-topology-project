#version 330 core
in vec2 ourTexCoord;
out vec4 fragColor;

uniform sampler2D map;
uniform sampler2D intensity;

/**
 * TODO: PART-1 update the fragment shader to get the texture coordinates from
 * the vertex shader
 */

/**
 * TODO: PART-3 update the fragment shader to get the fragColor color from the
 * texture, and add the sampler2D.
 */

void main() {
vec4 color = texture(map, ourTexCoord);
vec4 strength = texture(intensity, ourTexCoord);
    fragColor = vec4(clamp(color.x+500*strength.x, 0.0, 1.0), color.y, clamp(color.z+500*strength.z,0.0,1.0), color.w);

}
