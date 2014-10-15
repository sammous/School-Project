/* 1.Detect when enter key press 
   2.Detect when bracket is opened
   3.Detect when bracket is closed*/


//Enter pressed

private void textBox1_KeyDown(object sender, KeyEventArgs e)
    {
        if (e.Key == Key.Enter)
        {
            MessageBox.Show("Enter pressed");
        }
    }


/* Simulate tab pressed when enter key pressed */

 private void tabItem_PreviewKeyDown(object sender, KeyEventArgs e)
    {
      if (e.Key == Key.Enter)
      {
        TraversalRequest request = new TraversalRequest(FocusNavigationDirection.Right);
        request.Wrapped = true;
        (sender as TabItem).MoveFocus(request);
      }
    }
