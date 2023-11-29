/*Arduino OLED 动画线性函数*/

//初始参数
//目标参数
//速度 数值越大越慢
void animation(float *a, float *a_trg, uint8_t n)
{
  if (fabs(*a - *a_trg) < 0.15)
    *a = *a_trg;
  if (*a != *a_trg)
    *a += (*a_trg - *a) / (n / 10.0);
}
