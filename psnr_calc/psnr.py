import cv2



the_general_result_sr = 0
the_general_result_bileteral = 0
the_general_result_median = 0
the_general_result_other = 0
the_general_result_L0 = 0
the_general_result_L0_colored = 0
instance_number=7

for x in range(1,instance_number+1):
    test_number = "test" + str(x) #prefix of the image names to be tested
    img1 = cv2.imread(test_number+'_original.png') #first instances
    img2 = cv2.imread(test_number+'_sr.png') #second instances
    img3 = cv2.imread(test_number+'_bileteral.png')
    img4 = cv2.imread(test_number+'_median.png')
    img5 = cv2.imread(test_number+'_other.png')
    img6 = cv2.imread(test_number+'_L0.png')
    img7 = cv2.imread(test_number+'_L0_colored.png')

    psnr_result_sr = cv2.PSNR(img1, img2) 
    psnr_result_bileteral = cv2.PSNR(img1, img3)
    psnr_result_median = cv2.PSNR(img1, img4)
    psnr_result_other = cv2.PSNR(img1, img5)
    psnr_result_L0 = cv2.PSNR(img1, img6)
    psnr_result_L0_colored = cv2.PSNR(img1, img7)

    the_general_result_sr = the_general_result_sr + psnr_result_sr # add the total result
    the_general_result_bileteral = the_general_result_bileteral + psnr_result_bileteral
    the_general_result_median = the_general_result_median + psnr_result_median
    the_general_result_other = the_general_result_other + psnr_result_other
    the_general_result_L0 = the_general_result_L0 + psnr_result_L0
    the_general_result_L0_colored = the_general_result_L0_colored + psnr_result_L0_colored


print("sr_direct:",the_general_result_sr/7)
print("dst:",the_general_result_bileteral/7)
print("median:",the_general_result_median/7)
print("other:",the_general_result_other/7)
print("L0:",the_general_result_L0/7)
print("L0 colored:",the_general_result_L0_colored/7)


