require 'test_helper'


describe 'Sample' do
  it 'it should be ok' do
    s = Sample.new
    s.is_it_ok?.must_equal true
  end
  
end
