#include <inttypes.h>

typedef struct inputStruct
{
   float a[3];
   int b;
} input_t;

typedef struct outputStruct
{
   float u[3];
   uint8_t v;
   float w;
} output_t;

output_t returnSillyThings(const input_t * in)
{
   output_t out;
   for (unsigned int i = 0; i < 3; ++i)
   {
      out.u[i] = (2.0 + (float )i)*(in->a[i]);
   }
   out.v = (uint8_t )(in->b);
   out.w = (float )(in->b);

   return out;
}

void outArgsSillyThings(const input_t * in, output_t * out)
{
   for (unsigned int i = 0; i < 3; ++i)
   {
      out->u[i] = (2.0 + (float )i)*(in->a[i]);
   }
   out->v = (uint8_t )(in->b);
   out->w = (float )(in->b);
}
